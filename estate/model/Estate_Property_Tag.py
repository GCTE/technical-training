from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(
        required=True
    )

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise UserError("The property tag name must be unique.")