"""
Copyright 2014 Taxamo, Ltd.

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

class TaxamoStatsApiTest(TaxamoTest):
    def test_transactions_stats(self):
        resp = self.api.getTransactionsStats('2099-04-01', '2099-06-30',
                                             interval='month')

        self.assertEqual(resp.by_status.C[0].day, '2099-04-01')
        self.assertEqual(resp.by_status.C[1].day, '2099-05-01')
        self.assertEqual(resp.by_status.C[2].day, '2099-06-01')

    def test_settlement_stats_by_country(self):
        resp = self.api.getSettlementStatsByCountry('2099-04-01', '2099-06-30')

        self.assertEqual(resp.by_country, [])