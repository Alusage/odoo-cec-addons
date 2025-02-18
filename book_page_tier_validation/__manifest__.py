# @author: Armand Polmard (contact@arpol.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Book Page Tier Validation',
    'version': '1.0',
    'summary': 'Module that uses OCA base tier validation on the page model from cec_base',
    'author': 'ArPol',
    'website': 'https://arpol.fr',
    'category': 'Tools',
    'depends': ['base_tier_validation', 'cec_base'],
    'data': [
        'views/tier_validation_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}