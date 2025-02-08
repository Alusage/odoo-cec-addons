{
    'name': 'CEC Base',
    'version': '17.0.1.0.0',
    'summary': 'Base module for CEC customizations',
    'description': 'This module provides the base functionalities for CEC customizations in Odoo 17.0.',
    'author': 'Nicolas JEUDY',
    'website': 'https://www.yourcompanywebsite.com',
    'category': 'Custom',
    'depends': ['base', 'contacts'],
    'data': [
        'views/book_view.xml',
        'views/page_view.xml',
        "views/contribution_view.xml",
        "views/contribution_part_view.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [
        # List your demo files here
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}