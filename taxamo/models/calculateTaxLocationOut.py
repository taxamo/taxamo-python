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
class CalculateTaxLocationOut:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'tax_country_code': 'str',
            'tax_deducted': 'bool',
            'tax_supported': 'bool',
            'countries': 'countries',
            'buyer_ip': 'str',
            'billing_country_code': 'str',
            'buyer_credit_card_prefix': 'str',
            'evidence': 'evidence'

        }


        #Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode.
        self.tax_country_code = None # str
        #If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
        self.tax_deducted = None # bool
        #Is tax calculation supported for a detected tax location?
        self.tax_supported = None # bool
        #Map of countries calculated from evidence provided. This value is not stored and is available only upon tax calculation.
        self.countries = None # countries
        #IP address of the buyer in dotted decimal (IPv4) or text format (IPv6).
        self.buyer_ip = None # str
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        #First 6 digits of buyer's credit card prefix.
        self.buyer_credit_card_prefix = None # str
        #Tax country of residence evidence.
        self.evidence = None # evidence
        
