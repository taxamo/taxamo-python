#!/usr/bin/env python
"""
Copyright 2014-2021 by Taxamo

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
class Country:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'code_long': 'str',
            'codenum': 'str',
            'currency': 'list[str]',
            'tax_supported': 'bool',
            'name': 'str',
            'ccn3': 'str',
            'tax_region': 'str',
            'cca3': 'str',
            'callingCode': 'list[str]',
            'tax_number_country_code': 'str',
            'code': 'str',
            'cca2': 'str'

        }


        #Three letter ISO country code.
        self.code_long = None # str
        #Country ISO 3-digit code.
        self.codenum = None # str
        #List of currencies.
        self.currency = None # list[str]
        #True if tax calculation supported for this country.
        self.tax_supported = None # bool
        #Country name.
        self.name = None # str
        #Country ISO 3-digit code.
        self.ccn3 = None # str
        #Tax region code - e.g. EU, US, NO, JP...
        self.tax_region = None # str
        #Three letter ISO country code.
        self.cca3 = None # str
        #List of phone number calling codes.
        self.callingCode = None # list[str]
        #VAT number country code. Important for Greece.
        self.tax_number_country_code = None # str
        #Two letter ISO country code.
        self.code = None # str
        #Two letter ISO country code.
        self.cca2 = None # str
        
