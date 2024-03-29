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
class Captcha:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'riddle_key': 'str',
            'resolution_mode': 'str',
            'resolution_id': 'str',
            'image_base64': 'str',
            'solution': 'str'

        }


        #Captcha riddle key, has to be sent back with the captcha solution.
        self.riddle_key = None # str
        #Wait or schedule. wait returns the validation response in check_result and schedule returns a resolution_id to be used in a subsequent call with the riddle key. These modes may not be available for your integration.
        self.resolution_mode = None # str
        #
        self.resolution_id = None # str
        #Captcha image as base64. Used where it is not possible to direct the customer to captcha image URL. To display it in a browser, for example you can prefix it with &quot;data:image/png;base64, &quot; and use this as an image URL.
        self.image_base64 = None # str
        #Captcha solution provided by the human.
        self.solution = None # str
        
