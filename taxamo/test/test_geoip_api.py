import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TaxamoGeoIPApiTest(TaxamoTest):
    def test_ops(self):
        resp = self.api.locateMyIP()

        self.assertFalse(resp.country_code is None)

        resp = self.api.locateGivenIP("8.8.8.8")

        self.assertFalse(resp.country_code is "US")