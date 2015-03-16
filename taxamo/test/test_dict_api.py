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