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
class By_country:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'value': 'number',
            'tax_country_name': 'str',
            'tax_country_code': 'str',
            'currency_code': 'str'

        }


        #Tax amount
        self.value = None # number
        #Country name
        self.tax_country_name = None # str
        #Two letter ISO country code.
        self.tax_country_code = None # str
        #Three-letter ISO currency code.
        self.currency_code = None # str
        
