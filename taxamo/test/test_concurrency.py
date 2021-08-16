"""
Copyright 2021 Taxamo, Ltd.

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
from threading import Thread
from decimal import Decimal
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def make_transaction_data(total_amount):
    return {
        'currency_code': 'USD',
        'billing_country_code': 'IE',
        'tax_country_code': 'IE',
        'transaction_lines': [{'total_amount': total_amount,
                               'custom_id': 'line-100-1'}]
    }

transaction_data_100 = make_transaction_data(100)
transaction_data_200 = make_transaction_data(200)
transaction_data_300 = make_transaction_data(300)

def thread_fn(api, results):
    api_1 = api or taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))

    results.append([
        api_1.calculateTax({'transaction': transaction_data_100}).transaction.total_amount,
        api_1.calculateTax({'transaction': transaction_data_200}).transaction.total_amount,
        api_1.calculateTax({'transaction': transaction_data_300}).transaction.total_amount
    ])

class TaxamoConcurrencyTest(TaxamoTest):
    FORK_COUNT = 5
    THREAD_COUNT = 5

    def test_forks_apiapi_per_process(self):
        pids = []
        for n in range(self.FORK_COUNT):
            pid = os.fork()
            if pid == 0:
                api_1 = taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))
                self.assertEqual(api_1.calculateTax({'transaction': transaction_data_100}).transaction.total_amount, 100)
                os._exit(0)
            else:
                pids.append(pid)
                api_2 = taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))
                self.assertEqual(api_2.calculateTax({'transaction': transaction_data_200}).transaction.total_amount, 200)

        for pid in pids:
            os.waitpid(pid, 0)

    def test_forks_apiapi_per_process_multiple_requests(self):
        pids = []
        for n in range(self.FORK_COUNT):
            pid = os.fork()
            if pid == 0:
                api_1 = taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))
                self.assertEqual(api_1.calculateTax({'transaction': transaction_data_100}).transaction.total_amount, 100)
                self.assertEqual(api_1.calculateTax({'transaction': transaction_data_200}).transaction.total_amount, 200)
                self.assertEqual(api_1.calculateTax({'transaction': transaction_data_300}).transaction.total_amount, 300)
                os._exit(0)
            else:
                pids.append(pid)
                api_2 = taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))
                self.assertEqual(api_2.calculateTax({'transaction': transaction_data_100}).transaction.total_amount, 100)
                self.assertEqual(api_2.calculateTax({'transaction': transaction_data_200}).transaction.total_amount, 200)
                self.assertEqual(api_2.calculateTax({'transaction': transaction_data_300}).transaction.total_amount, 300)

        for pid in pids:
            os.waitpid(pid, 0)

    def test_threads_single_apiapi(self):
        api = taxamo.api.ApiApi(taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS))

        results = []
        threads = []

        for x in range(self.THREAD_COUNT):
            threads.append(Thread(target=thread_fn, args=(api, results,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(results,  self.THREAD_COUNT * [[Decimal(100), Decimal(200), Decimal(300)]])

    def test_threads_apiapi_per_thread(self):
        results = []
        threads = []
        for x in range(self.THREAD_COUNT):
            threads.append(Thread(target=thread_fn, args=(None, results,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(results,  self.THREAD_COUNT * [[Decimal(100), Decimal(200), Decimal(300)]])

