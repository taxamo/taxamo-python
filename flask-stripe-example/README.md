## Taxamo, Stripe & Flask

This guide enhances [Stripe's Flask guide](https://stripe.com/docs/checkout/guides/flask) to support Taxamo tax calculation
and transaction confirmation and to serve as an example for integration with Python apps.

*Complete source codes for this example are located in `flask-stripe-example` directory for `taxamo-python`.*

It assumes that some details for a customer are known/set - billing country and a customer's name.

As Stripe and Flask are already installed, we just need to install taxamo Python bindings. 
To do so, just go to `taxamo-python` source directory and type:

```
sudo python setup.py install
```

### Setting up taxamo API

To access taxamo API from Python, we need to import appropriate packages in `app.py`:

```
import taxamo.api
import taxamo.swagger
import taxamo.error
```

Initialize the API:

```
taxamo_api = taxamo.api.ApiApi(taxamo.swagger.ApiClient(apiKey=os.environ['TAXAMO_PRIVATE_TOKEN'],
                                                        apiServer='https://beta.taxamo.com'))
```

We're using `TAXAMO_PRIVATE_TOKEN` environment variable. It is recommended to use test token for this tutorial.

We will also be using sessions, so for example we use cookie-based implementation (please remember to update secret_key to a different value):

```
app.secret_key = '\xa7Ca\xc5|w\xf6\x9a\x9a\xae\xa6\x87\xce\xf8\xa8\x82\xd7\xea\x96Kz\x9a\xf4\xae'
```

### Pre-calculating tax

Before we proceed with the transaction, we should present the actual price to the customer. We can use customer's IP
 address to guess their country, but we need to provide them with ability to alter that information.
 
To do so, we need to enhance our `index` function in `app.py` to support that:

```
@app.route('/')
def index():
    #simplify billing country information
    if 'billing_country_code' not in session:
        ip_data = taxamo_api.locateGivenIP(request.remote_addr)
        session['billing_country_code'] = ip_data.country_code
        
    tax_resp = taxamo_api.calculateTax({'transaction': {
        'currency_code': 'USD',
        'buyer_ip': request.remote_addr,
        #force country code makes sense only if the customer will provide additional details later on
        'force_country_code': session['billing_country_code'],
        'billing_country_code': session['billing_country_code'],
        'transaction_lines': [{'amount': 5, 'custom_id': 'line1'}]
    }})
    return render_template('index.html',
                           key=stripe_keys['publishable_key'],
                           total_amount=tax_resp.transaction.total_amount,
                           tax_rate=tax_resp.transaction.transaction_lines[0].tax_rate,
                           billing_country_code=session['billing_country_code'],
                           ip_country_code=tax_resp.transaction.countries.by_ip.code,
                           tax_country_code=tax_resp.transaction.tax_country_code,
                           countries=taxamo_api.getCountriesDict().dictionary)
```

First, if the billing country is not set, we guess it from IP address using `taxamo_api.locateGivenIP`. Next we calculate 
tax, forcing customer's billing country for a VAT rate as we don't know the credit card number BIN/country of issue.

We can also present the customer with tax rate, detected country and ability to update billing country to something else
in `templates/index.html`:

```
{% extends "layout.html" %}
{% block content %}
<form action="/set_country" method="POST">
    <article>
        <label>
            <span>Amount is <b>${{ format_price(total_amount) }}</b></span>,

            {% if tax_rate %}
               <span>VAT rate is <b>{{ format_price(tax_rate) }}%</b></span>,
            {% endif %}
            <span>Detected country is: {{ ip_country_code }}</span>,
            {% if tax_rate %}
                <span>TAX country is: {{ tax_country_code }}</span>,
            {% endif %}
            <span>Billing country is:
                <select name="billing_country_code">
                    {% for country in countries %}
                        <option value="{{ country.code }}"
                                {% if country.code == billing_country_code %}
                                    selected="1"
                                {% endif %}
                                >{{ country.code }} - {{ country.name }}</option>
                    {% endfor %}
                </select>
                <button type="submit">Update</button>
            </span>

            {% if billing_country_code != ip_country_code %}
                <h5>Warning</h5>
                <ul>
                    <li>Billing country code set to: <b>{{ billing_country_code }}</b></li>
                    <li>Computer's country code detected as from: <b>{{ ip_country_code }}</b></li>
                </ul>
                <p>Tax calculated for:  <b>{{ billing_country_code }}</b>, but credit card issued in <b>{{billing_country_code}}</b> will need to be used.</p>
            {% endif %}
        </label>

    </article>
</form>


<form action="/charge" method="post">
    <script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
            data-key="{{ key }}"
            data-description="A Flask Charge"
            data-amount="{{ format_int(total_amount * 100)}}"></script>
</form>
{% endblock %}
```

As we have allowed the customer to update their billing country on payment form, we need to add appropriate
controller to `app.py`:

```
@app.route('/set_country', methods=['POST'])
def set_country():
    session['billing_country_code'] = request.form['billing_country_code']
    return redirect('/')
```

We also need a processor for proper formatting of numbers in our templates. Let's just add it to `app.py`:

```
@app.context_processor
def utility_processor():
    def format_price(amount):
        if amount:
            return u'{0:.2f}'.format(amount)
        else:
            return None
    def format_int(amount):
        if amount:
            return u'{0:.0f}'.format(amount)
        else:
            return None
    return dict(format_price=format_price, format_int=format_int)
```


### Payment and Taxamo transaction storage

Once the payment has been initiated by the user and Stripe.js has collected credit card details.

To do so, we need to enhance `charge()` controller to contact Taxamo to validate tax evidence by storing a
transaction and once the payment is accepted by Stripe, confirm transaction in Taxamo to make it appear
on the settlement.

```
@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    token = stripe.Token.retrieve(request.form['stripeToken'])

    #simplify billing country information
    if 'billing_country_code' not in session:
        ip_data = taxamo_api.locateGivenIP(request.remote_addr)
        session['billing_country_code'] = ip_data.country_code

    try:
        resp = taxamo_api.createTransaction({'transaction': {
            'currency_code': 'USD',
            'buyer_ip': request.remote_addr,
            'buyer_name': 'John Doe', #that should be collected from a user
            'evidence': {'by_payment_method': {'evidence_value': token.card.country}},
            'billing_country_code': session['billing_country_code'],
            'transaction_lines': [{'amount': 5, 'custom_id': 'line1'}]
        }})
        amount = resp.transaction.total_amount
        if resp.transaction.tax_country_code != session['billing_country_code']:
            return redirect('/wrong_card?code=' + token.card.country)

    except taxamo.error.ValidationError: #we might need to dive into the error details
        return redirect('/wrong_card?code=' + token.card.country)

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=int(amount*100),
        currency='usd',
        description='Flask Charge'
    )

    taxamo_api.confirmTransaction(resp.transaction.key, {'transaction': {'invoice_place': 'Someplace'}})

    return render_template('charge.html', amount=int(amount*100))
```

As we don't have access to credit card country earlier in this approach (Stripe.js popup form takes care of credit card number), 
we need to make sure, that the new piece of evidence hasn't changed the tax country. If the form would be embedded
in our HTML file, we might read the credit card's BIN and propagate it to taxamo using `taxamo.js`. 

```
@app.route('/wrong_card')
def wrong_card():
    return render_template('wrong_card.html', code=request.args.get('code'))
```

And we need the template `wrong_card.html`:

```
{% extends "layout.html" %}
{% block content %}
<h2>Your card was issued in {{ code }}, but other evidence points to different countries.</h2>
<a href="/">Try again</a>
{% endblock %}
```

Finally, we should display dynamic amount after the transaction was successful, so we have
to update `templates/charge.html`:

```
{% extends "layout.html" %}
{% block content %}
<h2>Thanks, you paid <strong>$ {{ format_price(amount/100) }}</strong>!</h2>
{% endblock %}
```

## Running the sample

With all the changes applied, we can run the code:
 
```
PUBLISHABLE_KEY=pk_test_wlmUwh5iKQSAaesWKFrQX7oj SECRET_KEY=sk_test_F1lO6aFaLncuLd8AAkUEgjBw TAXAMO_PRIVATE_TOKEN='SamplePrivateTestKey1' python app.py
```