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
class CreateRefundIn:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'line_key': 'str',
            'custom_id': 'str',
            'refund_timestamp': 'str',
            'amount': 'number',
            'total_amount': 'number',
            'refund_reason': 'str',
            'refund_unique_id': 'str'

        }


        #Line identifier. If neither line key or custom id is provided, the refund amount will be assigned to lines in order.
        self.line_key = None # str
        #Line custom identifier. If neither line key or custom id is provided, the refund amount will be assigned to lines in order.
        self.custom_id = None # str
        #Refund timestamp in yyyy-MM-dd HH:mm:ss or yyyy-MM-dd'T'HH:mm:ss'Z' format. No timezone conversion is applied.
        self.refund_timestamp = None # str
        #Amount (without tax) to be refunded. Either amount or total amount is required. In case of line key and custom id missing, only total_amount can be used.
        self.amount = None # number
        #Total amount, including tax, to be refunded. Either amount or total amount is required. In case of line key and custom id missing, only total_amount can be used.
        self.total_amount = None # number
        #Refund reason, displayed on the credit note.
        self.refund_reason = None # str
        #Refund custom identifier.
        self.refund_unique_id = None # str
        
