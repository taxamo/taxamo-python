#!/usr/bin/env python
"""
Copyright 2014-2015 Taxamo, Ltd.

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
class Transaction_lines:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'product_type': 'str',
            'deducted_tax_amount': 'number',
            'deducted_tax_rate': 'number',
            'supply_date': 'str',
            'invoice_image_url': 'str',
            'tax_number_service': 'str',
            'seller_tax_number': 'str',
            'id': 'number',
            'tax_supported': 'bool',
            'unit_price': 'number',
            'unit_of_measure': 'str',
            'quantity': 'number',
            'custom_fields': 'list[custom_fields]',
            'tax_region': 'str',
            'line_key': 'str',
            'invoice_number': 'str',
            'product_class': 'str',
            'tax_name': 'str',
            'product_code': 'str',
            'amount': 'number',
            'invoice_image_url_secret': 'str',
            'custom_id': 'str',
            'informative': 'bool',
            'tax_amount': 'number',
            'tax_entity_additional_id': 'str',
            'ship_from_country_code': 'str',
            'tax_rate': 'number',
            'additional_currencies': 'additional_currencies',
            'total_amount': 'number',
            'product_tax_code': 'str',
            'tax_entity_name': 'str',
            'refunded_tax_amount': 'number',
            'description': 'str',
            'tax_deducted': 'bool',
            'tax_country_code': 'str',
            'refunded_total_amount': 'number'

        }


        #Product type, according to dictionary /dictionaries/product_types. 
        self.product_type = None # str
        #Deducted tax amount, calculated by taxmo.
        self.deducted_tax_amount = None # number
        #Deducted tax rate, calculated by taxamo.
        self.deducted_tax_rate = None # number
        #Date of supply in yyyy-MM-dd format.
        self.supply_date = None # str
        #Invoice image URL - provided by Taxamo.
        self.invoice_image_url = None # str
        #Tax number service identifier - if available for a given region and the region is enabled.
        self.tax_number_service = None # str
        #Seller's tax number in the tax country - used for physical goods and assigned from merchant configuration.
        self.seller_tax_number = None # str
        #Generated id.
        self.id = None # number
        #Is tax supported on this line.
        self.tax_supported = None # bool
        #Unit price.
        self.unit_price = None # number
        #Unit of measure.
        self.unit_of_measure = None # str
        #Quantity Defaults to 1.
        self.quantity = None # number
        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Tax region code - e.g. EU, US, NO, JP...
        self.tax_region = None # str
        #Generated line key.
        self.line_key = None # str
        #Invoice number.
        self.invoice_number = None # str
        #Product class
        self.product_class = None # str
        #Tax name, calculated by taxamo.  Can be overwritten when informative field is true.
        self.tax_name = None # str
        #Internal product code, used for invoicing for example.
        self.product_code = None # str
        #Amount. Required if total amount or both unit price and quantity are not provided.
        self.amount = None # number
        #Invoice image URL secret - provided by Taxamo.
        self.invoice_image_url_secret = None # str
        #Custom id, provided by ecommerce software.
        self.custom_id = None # str
        #If the line is provided for informative purposes. Such line must have :tax-rate and optionally :tax-name - if not, API validation will fail for this line.
        self.informative = None # bool
        #Tax amount, calculated by taxamo.
        self.tax_amount = None # number
        #Tax entity additional id.
        self.tax_entity_additional_id = None # str
        #Two-letter ISO country code, e.g. FR.
        self.ship_from_country_code = None # str
        #Tax rate, calculated by taxamo. Must be provided when informative field is true.
        self.tax_rate = None # number
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        #Total amount. Required if amount or both unit price and quantity are not provided.
        self.total_amount = None # number
        #External product tax code for a line, for example TIC in US Sales tax.
        self.product_tax_code = None # str
        #To which entity is the tax due.
        self.tax_entity_name = None # str
        #Refunded tax amount, calculated by taxmo.
        self.refunded_tax_amount = None # number
        #Line contents description.
        self.description = None # str
        #True if the transaction line is deducted from tax and no tax is applied (it is untaxed).
        self.tax_deducted = None # bool
        #Two-letter ISO country code, e.g. FR.
        self.tax_country_code = None # str
        #Refunded total amount, calculated by taxmo.
        self.refunded_total_amount = None # number
        
