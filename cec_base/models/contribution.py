from odoo import api,models, fields


class ContributionPart(models.Model):
    _name = 'cec_base.contribution.part'
    _description = 'Element de Contribution'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    date = fields.Date(related="contribution_id.date",string='Date', store=True)
    contribution_id = fields.Many2one('cec_base.contribution', string='Contribution')
    contributor_id = fields.Many2one(related='contribution_id.contributor_id', string='Contributor', store=True)
    page_id = fields.Many2one('cec_base.book.page', string='Page')
    raw_content = fields.Html(string='Raw Content', tracking=True)
    content = fields.Html(string='Content', tracking=True)
    book_id = fields.Many2one(related="page_id.book_id", string='Book', required=True)
    assigned_user_ids = fields.Many2many('res.users', string='Assigned Users')

    @api.onchange('page_id', 'contributor_id')
    def _onchange_book_page(self):
        if self.page_id:
            self.name = f"[{self.book_id.name}] Page {self.page_id.page_number}"
        if self.page_id and self.contributor_id:
            self.name = f"[{self.book_id.name}] Page {self.page_id.page_number} - {self.contributor_id.name}"

class Contribution(models.Model):
    _name = 'cec_base.contribution'
    _description = 'Contribution'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    page_ids = fields.Many2many('cec_base.book.page', relation='page_contribution_rel', string='Pages')
    date = fields.Date(string='Date', required=True)
    contributor_id = fields.Many2one('res.partner', string='Contributor', required=True)
    raw_content = fields.Html(string='Raw Content')
    content = fields.Html(string='Content')

    @api.onchange('date', 'contributor_id')
    def _onchange_book_page(self):
        if self.date and self.contributor_id:
            self.name = f"[{self.date}] {self.contributor_id.name}"