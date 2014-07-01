import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TaxamoReportsApiTest(TaxamoTest):
    def test_settlement_report(self):
        resp = self.api.getSettlementReport('2099-04')

        self.assertEqual(resp.start_date, '2099-04-01T00:00:00Z')
        self.assertEqual(resp.end_date, '2099-06-30T23:59:59Z')
        self.assertEqual(resp.report[0].total_amount, 0)
