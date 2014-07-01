import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TaxamoStatsApiTest(TaxamoTest):
    def test_transactions_stats(self):
        resp = self.api.getTransactionsStats('2099-04-01', '2099-06-30',
                                             interval='month')

        self.assertEqual(resp.by_status.N[0].day, '2099-04-01')
        self.assertEqual(resp.by_status.N[1].day, '2099-05-01')
        self.assertEqual(resp.by_status.N[2].day, '2099-06-01')
        self.assertEqual(resp.by_status.C[0].day, '2099-04-01')
        self.assertEqual(resp.by_status.C[1].day, '2099-05-01')
        self.assertEqual(resp.by_status.C[2].day, '2099-06-01')

    def test_settlement_stats_by_country(self):
        resp = self.api.getSettlementStatsByCountry('2099-04-01', '2099-06-30')

        self.assertEqual(resp.by_country, [])

    def test_settlement_stats_by_taxation_type(self):
        resp = self.api.getSettlementStatsByTaxationType('2099-04-01', '2099-06-30')

        self.assertEqual(resp.by_taxation_type.taxed_count, 0)
        self.assertEqual(resp.by_taxation_type.deducted_count, 0)
        self.assertEqual(resp.by_taxation_type.transactions_count, 0)

