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
import time
import unittest
import threading
import BaseHTTPServer

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import taxamo.error
import taxamo.http_client
import taxamo.swagger
import taxamo.api

class TimedOutHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        time.sleep(2)
        return

    def log_message(self, format, *args):
        return

class TaxamoApiConnectivityTest(TaxamoTest):

    def test_validate(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
        api = taxamo.api.ApiApi(api_client)
        self.assertRaises(
            taxamo.error.ValidationError,
            lambda: api.calculateTax(
                {
                    '__transaction': {
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
                    }}))
        api_client.client = taxamo.http_client.Urllib2Client()

        api = taxamo.api.ApiApi(api_client)
        self.assertRaises(
            taxamo.error.ValidationError,
            lambda: api.calculateTax(
                {
                    '__transaction': {
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
                    }}))


    def test_auth(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN + "!", TEST_ADDRESS)
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.AuthenticationError,
            lambda: api.getTransaction("non-existent"))

        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.AuthenticationError,
            lambda: api.getTransaction("non-existent"))

    def test_wrong_host(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN + "!", "http://i-dont-exist.taxamo.com.nonexistent:123")
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.APIConnectionError,
            lambda: api.getCurrenciesDict())

        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        self.assertRaises(
            taxamo.error.APIConnectionError,
            lambda: api.getCurrenciesDict())

    def test_urllib2(self):
        api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
        api_client.client = taxamo.http_client.Urllib2Client()
        api = taxamo.api.ApiApi(api_client)

        resp = api.calculateTax(
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

    def test_timeout(self):
        server = BaseHTTPServer.HTTPServer((TEST_SERVER_HOST, TEST_SERVER_PORT), TimedOutHandler)
        t = threading.Thread(target=lambda: server.serve_forever())
        t.start()
        time.sleep(0.2) # naive - await server creation

        try:
            api_client_urllib2 = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_SERVER_PROTOCOL + TEST_SERVER_HOST + ':' + str(TEST_SERVER_PORT), 1)
            api_client_urllib2.client = taxamo.http_client.Urllib2Client()
            api_urllib2 = taxamo.api.ApiApi(api_client_urllib2)

            self.assertRaises(
                taxamo.error.APIConnectionError,
                lambda: api_urllib2.calculateTax({
                            'transaction': {
                                'currency_code': 'USD',
                                'buyer_ip': '127.0.0.1',
                                'billing_country_code': 'IE',
                                'force_country_code': 'FR',
                                'transaction_lines': [{'amount': 200,
                                                       'custom_id': 'line1'},
                                                      {'amount': 100,
                                                       'product_type': 'e-book',
                                                       'custom_id': 'line2'}]}}))

            api_client_requests = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_SERVER_PROTOCOL + TEST_SERVER_HOST + ':' + str(TEST_SERVER_PORT), 1)
            api_client_requests.client = taxamo.http_client.RequestsClient()
            api_requests = taxamo.api.ApiApi(api_client_requests)

            self.assertRaises(
                taxamo.error.APIConnectionError,
                lambda: api_requests.calculateTax({
                            'transaction': {
                                'currency_code': 'USD',
                                'buyer_ip': '127.0.0.1',
                                'billing_country_code': 'IE',
                                'force_country_code': 'FR',
                                'transaction_lines': [{'amount': 200,
                                                       'custom_id': 'line1'},
                                                      {'amount': 100,
                                                       'product_type': 'e-book',
                                                       'custom_id': 'line2'}]}}))
        finally:
            server.shutdown()






