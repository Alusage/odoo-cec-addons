from odoo import api,models, fields

class Book(models.Model):
    _name = 'cec_base.book'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    location = fields.Many2one('res.partner', string='Location')
    published_date = fields.Date(string='Published Date')
    description = fields.Text(string='Description')
    page_ids = fields.One2many('cec_base.book.page', 'book_id', string='Pages')
    page_count = fields.Integer(string='Page Count', compute='_compute_page_count')

    @api.depends('page_ids')
    def _compute_page_count(self):
        for book in self:
            book.page_count = len(book.page_ids)

    def action_show_pages(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pages',
            'view_mode': 'tree,form',
            'res_model': 'cec_base.book.page',
            'domain': [('book_id', '=', self.id)],
            'context': dict(self.env.context, default_book_id=self.id),
        }