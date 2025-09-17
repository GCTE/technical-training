from odoo import models, fields, api

class EstatePropertyTypeInLine(models.Model):
    _name = "estate.property.type.inline"
    _description = "Estate Property Type Inline"

    name = fields.Char(
        required=True,
    )
    
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    # field_1 = fields.Char()
    # field_2 = fields.Char()
    # field_3 = fields.Char()