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
