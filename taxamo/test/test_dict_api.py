import os
import sys
import unittest

from helper import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

class TaxamoDictApiTest(TaxamoTest):
    def test_countries_dict(self):
        resp = self.api.getCountriesDict()

        self.assertFalse(resp.dictionary[0].code is None)
        self.assertFalse(resp.dictionary[0].name is None)
        self.assertEqual(resp.dictionary[0].cca2, resp.dictionary[0].code)


    def test_currencies_dict(self):
        resp = self.api.getCurrenciesDict()

        self.assertFalse(resp.dictionary[0].code is None)
        self.assertFalse(resp.dictionary[0].minorunits is None)

    def test_product_types_dict(self):
        resp = self.api.getProductTypesDict()

        self.assertFalse(resp.dictionary[0].code is None)