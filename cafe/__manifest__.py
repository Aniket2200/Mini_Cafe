# -*- coding: utf-8 -*-
{
    'name': "Cafe Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': '-100',
    'application': True,


    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/newcafe.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/staff_members.xml',
        'views/inventory.xml',
        'views/category.xml',
        'views/main_inventory.xml',
        'views/order.xml',
        'views/product.xml',
        'views/product2.xml',
        'report/report.xml',
        'report/order_report.xml',
        'views/menu.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
