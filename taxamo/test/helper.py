TEST_TOKEN='SamplePrivateTestKey1'
TEST_ADDRESS='https://beta.taxamo.com'
#TEST_ADDRESS='http://localhost:3007'

import taxamo.swagger
import taxamo.api
import unittest

default_api_client = taxamo.swagger.ApiClient(TEST_TOKEN, TEST_ADDRESS)
default_api = taxamo.api.ApiApi(default_api_client)

class TaxamoTest(unittest.TestCase):
    api_client = default_api_client
    api = default_api
