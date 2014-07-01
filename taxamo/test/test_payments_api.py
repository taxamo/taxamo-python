import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from taxamo.models.createPaymentIn import *

class TaxamoPaymentsApiTest(TaxamoTest):
    def test_ops(self):
        resp = self.api.createTransaction(
            {
                'transaction': {
                    'currency_code': 'USD',
                    'buyer_ip': '127.0.0.1',
                    'billing_country_code': 'IE',
                    'force_country_code': 'FR',
                    'buyer_name': "Payment test",
                    'transaction_lines': [{'amount': 200,
                                           'custom_id': 'line1'},
                                          {'amount': 100,
                                           'product_type': 'e-book',
                                           'custom_id': 'line2'}]
                }})
        self.assertFalse(resp.transaction.key is None)

        resp = self.api.getTransaction(resp.transaction.key)

        self.assertFalse(resp.transaction.key is None)
        self.assertEqual(resp.transaction.status, 'N')

        payment_in = CreatePaymentIn()
        payment_in.amount = 10
        payment_in.payment_information = "Test payment #1"
        payment_in.payment_timestamp = "2014-06-23T23:00:00.000Z"

        payment_resp = self.api.createPayment(resp.transaction.key, payment_in)

        self.assertEqual(payment_resp.success, True)