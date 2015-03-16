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

from taxamo.models.createSMSTokenIn import *

class TaxamoVerificationApiTest(TaxamoTest):
    def test_ops(self):
        req_in = CreateSMSTokenIn()

        req_in.country_code = "PL"
        req_in.recipient = "500600700"

        self.api.createSMSToken(req_in)
