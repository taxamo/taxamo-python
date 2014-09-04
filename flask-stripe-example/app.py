import os
from flask import Flask, render_template, request, session, redirect
import stripe
import taxamo.api
import taxamo.swagger
import taxamo.error

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.secret_key = '\xa7Ca\xc5|w\xf6\x9a\x9a\xae\xa6\x87\xce\xf8\xa8\x82\xd7\xea\x96Kz\x9a\xf4\xae'

taxamo_api = taxamo.api.ApiApi(taxamo.swagger.ApiClient(apiKey=os.environ['TAXAMO_PRIVATE_TOKEN'],
                                                        apiServer='https://api.taxamo.com'))

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

@app.route('/set_country', methods=['POST'])
def set_country():
    session['billing_country_code'] = request.form['billing_country_code']
    return redirect('/')


@app.route('/wrong_card')
def wrong_card():
    return render_template('wrong_card.html', code=request.args.get('code'))

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

if __name__ == '__main__':
    app.run(debug=True)