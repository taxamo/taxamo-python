"""
Copyright 2014-2021 by Taxamo

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TaxamoRefundsApiTest(TaxamoTest):
    def test_refund(self):
        resp = self.api.createTransaction(
            {
                'transaction': {
                    'status': 'C',
                    'currency_code': 'USD',
                    'buyer_ip': '127.0.0.1',
                    'billing_country_code': 'IE',
                    'force_country_code': 'FR',
                    'transaction_lines': [{'amount': 200,
                                           'custom_id': 'line1'},
                                          {'amount': 100,
                                           'product_type': 'e-book',
                                           'custom_id': 'line2'}]
                }})
        self.assertFalse(resp.transaction.key is None)
        self.assertEqual(resp.transaction.status, 'C')

        resp = self.api.createRefund(resp.transaction.key, {'total_amount': 10})

        self.assertEqual(resp.total_amount, 10)








