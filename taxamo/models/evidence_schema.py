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
class Evidence_schema:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'used': 'bool',
            'resolved_country_code': 'str',
            'evidence_type': 'str',
            'evidence_value': 'str'

        }


        #If the evidence was used to match the actual country.
        self.used = None # bool
        #Country code that was resolved using this evidence.
        self.resolved_country_code = None # str
        #Type of evidence.
        self.evidence_type = None # str
        #Value provided as evidence - for example IP address.
        self.evidence_value = None # str
        
