from odoo import api,models, fields

class BookPage(models.Model):
    _name = 'cec_base.book.page'
    _inherit = ['mail.activity.mixin', 'mail.thread.main.attachment']
    _description = 'Book Page'
    _order = 'page_number asc'

    state = fields.Selection([
        ('draft', 'Bouillon'),
        ('assigned', 'Affecté'),
        ('in_progress', 'En cours'),
        ('to_validate', 'À valider'),
        ('done', 'Terminé')
    ], string='State', default='draft', tracking=True)
    name = fields.Char(string='Title', required=True)
    raw_content = fields.Text(string='Raw Content')
    content = fields.Html(string='Content')
    page_number = fields.Integer(string='Page Number', required=True)
    book_id = fields.Many2one('cec_base.book', string='Book', required=True)
    contribution_ids = fields.Many2many('cec_base.contribution', relation='page_contribution_rel', string='Contributions')
    assigned_user_ids = fields.Many2many('res.users', string='Assigned Users')

    @api.onchange('book_id', 'page_number')
    def _onchange_book_page(self):
        if self.book_id and self.page_number:
            self.name = f"[{self.book_id.name}] Page {self.page_number}"

    def action_assign_to_me(self):
        self.ensure_one()
        self.assigned_user_ids = [(4, self.env.uid)]

    @api.onchange('assigned_user_ids')
    def _onchange_assigned_user_ids(self):
        if self.assigned_user_ids:
            self.state = 'assigned'
        else:
            self.state = 'draft'