import taxamo.api
import taxamo.swagger

print "Calculating tax"

apiClient = taxamo.swagger.ApiClient("SamplePrivateTestKey1", "https://api.taxamo.com")
api = taxamo.api.ApiApi(apiClient)

resp = api.calculateTax(
    {
        'transaction': {
            'currency_code': 'USD',
            'buyer_ip': '127.0.0.1',
            'billing_country_code': 'IE',
            'force_country_code': 'IE',
            'transaction_lines': [{'amount': 200,
                                   'custom_id': 'line1'}]
        }})

print "Detected country: %s" % (resp.transaction.countries.detected.code)
print "Original amount: %d, tax amount: %d, total: %d" % (resp.transaction.amount,
                                                          resp.transaction.tax_amount,
                                                          resp.transaction.total_amount)
