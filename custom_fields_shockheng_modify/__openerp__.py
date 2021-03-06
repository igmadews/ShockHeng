# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Fields Modifier Module',
    'version': '1.2',
    'category': 'Sale',
    'summary': 'Custom Fields Shockheng Modify',
    'description': """
    This module generates modification in fields for Shockheng 
    """,
    'author': 'HashMicro / GeminateCS',
    'website': 'www.hashmicro.com', 
    'depends': [
        'custom_sale_order_custmization',
        'PaymentTerm_SO_Custom',
        'purchase_shockheng_modifier',
        'account',
    ],
    'data': [
             'views/sale_view.xml',
             'views/purchase_order_view.xml',
             'views/product_view.xml',
             'views/account_invoice_view.xml',
             'wizard/b2b_and_b2c_summary_view.xml',
             'report/b2b_and_b2c_summary_report_view.xml',
             'wizard/outstanding_payment_view.xml',
             'report/outstanding_payment_report_view.xml',
             'report/report_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}