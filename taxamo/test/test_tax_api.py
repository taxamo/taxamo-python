import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TaxamoTaxApiTest(TaxamoTest):

    def test_calculate(self):
        resp = self.api.calculateTax(
            {
                'transaction': {
                    'currency_code': 'USD',
                    'buyer_ip': '127.0.0.1',
                    'billing_country_code': 'IE',
                    'force_country_code': 'FR',
                    'transaction_lines': [{'amount': 200,
                                           'custom_id': 'line1'},
                                          {'amount': 100,
                                           'product_type': 'e-book',
                                           'custom_id': 'line2'}
                    ]
                }})
        self.assertEqual(resp.transaction.countries.detected.code, "IE")
        self.assertEqual(resp.transaction.amount, 300)
        self.assertEqual(resp.transaction.tax_amount, 44.7)
        self.assertEqual(resp.transaction.total_amount, 344.7)

        self.assertEqual(resp.transaction.transaction_lines[0].custom_id, 'line1')
        self.assertEqual(resp.transaction.transaction_lines[0].tax_rate, 19.6)
        self.assertEqual(resp.transaction.transaction_lines[0].tax_amount, 39.2)
        self.assertEqual(resp.transaction.transaction_lines[1].custom_id, 'line2')
        self.assertEqual(resp.transaction.transaction_lines[1].tax_rate, 5.5)
        self.assertEqual(resp.transaction.transaction_lines[1].tax_amount, 5.5)

    def test_simple_calculate(self):
        resp = self.api.calculateSimpleTax(currency_code='USD',
                                     billing_country_code= 'IE',
                                     force_country_code='FR',
                                     amount=100,
                                     product_type='e-book')

        self.assertEqual(resp.transaction.tax_country_code, 'FR')
        self.assertEqual(resp.transaction.amount, 100)
        self.assertEqual(resp.transaction.tax_amount, 5.5)
        self.assertEqual(resp.transaction.total_amount, 105.5)

        self.assertEqual(resp.transaction.transaction_lines[0].tax_rate, 5.5)
        self.assertEqual(resp.transaction.transaction_lines[0].tax_rate, 5.5)
        self.assertEqual(resp.transaction.transaction_lines[0].total_amount, 105.5)

    def test_validate_tax_number(self):

        resp = self.api.validateTaxNumber("IE6388047V")

        self.assertEqual(resp.tax_deducted, True)
        self.assertEqual(resp.billing_country_code, "IE")

        resp = self.api.validateTaxNumber("IE6388047V12121")

        self.assertEqual(resp.tax_deducted, False)

    def test_location_calculate(self):

        resp = self.api.calculateTaxLocation(billing_country_code='BE',
                                             buyer_credit_card_prefix='424242')

        self.assertEqual(resp.tax_country_code, "BE")
        self.assertEqual(resp.tax_supported, True)
        self.assertEqual(resp.countries.detected.code, "BE")
        self.assertEqual(resp.countries.by_billing.code, "BE")
        self.assertEqual(resp.countries.by_cc.code, "BE")
