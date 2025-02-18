from odoo import models, fields, api, tools
from dateutil.relativedelta import relativedelta
from odoo.tools.translate import _
import pdb

class BookPage(models.Model):
    _name = "cec_base.book.page"
    _inherit = ["cec_base.book.page", "tier.validation"]
    _state_from = ["to_validate"]
    _state_to = ["done"]
    _cancel_state = "draft"

    _tier_validation_manual_config = False
    
    def validate_tier(self):
        super().validate_tier()
        if self.validated and self._name == "cec_base.book.page":
            self.write({"state": "done"})

    def write(self, vals):
        res = super(BookPage, self).write(vals)
        if 'state' in vals and vals['state'] == 'to_validate':
            self.request_validation()
        return res
