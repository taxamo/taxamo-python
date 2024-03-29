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
class Additional_interactions:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'requested': 'bool',
            'captcha': 'captcha',
            'interaction_kind': 'str',
            'interaction_result': 'str',
            'interaction_result_message': 'str',
            'region_key': 'str',
            'required': 'bool',
            'interaction_key': 'str',
            'interaction_prompt_message': 'str',
            'force_valid': 'bool'

        }


        #Should Taxamo trigger this interaction (e.g. request the captcha image) if possible. Please note this will increase the request time as we have to reach out to external resources.
        self.requested = None # bool
        #Captcha-specific information
        self.captcha = None # captcha
        #Kind of the interaction, e.g. b2b-captcha
        self.interaction_kind = None # str
        #Interaction result. For b2b-captcha it will be valid|invalid|error|expired.
        self.interaction_result = None # str
        #Interaction result message, useful in case there is an error.
        self.interaction_result_message = None # str
        #Region key for this interaction, e.g. IN or EU.
        self.region_key = None # str
        #On validation error, false returns the transaction tax calculation result and a warning (response 200). true will return an error and warning (response 400).
        self.required = None # bool
        #Key regarding the interaction, e.g. india-b2b-captcha
        self.interaction_key = None # str
        #Message that can be presented in the UI requesting for the interaction.
        self.interaction_prompt_message = None # str
        #Regardless of other flags in this interaction, treat the validation as successful. This for example can be used to display the prices without tax in the case of captcha-based B2B validation - when we don't want to show captchas for every tax calculation call.
        self.force_valid = None # bool
        
