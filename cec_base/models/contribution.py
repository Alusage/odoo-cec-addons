from odoo import models, fields

class Contribution(models.Model):
    _name = 'cec_base.contribution'
    _description = 'Contribution'

    name = fields.Char(string='Name', required=True)
    page_ids = fields.Many2many('cec_base.page', relation='page_contribution_rel', string='Pages')
    date = fields.Date(string='Date', required=True)
    contributor_id = fields.Many2one('res.partner', string='Contributor', required=True)
    raw_content = fields.Text(string='Raw Content')
    content = fields.Html(string='Content')
    scan = fields.Binary(string='Scan')