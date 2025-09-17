from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(
        required=True,
    )

    #List all the properties of the current type
    property_type_ids = fields.One2many("estate.property", "property_type_id")
    
    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise UserError("The property type name must be unique.")