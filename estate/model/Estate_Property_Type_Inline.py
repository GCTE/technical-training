from odoo import models, fields, api

class EstatePropertyTypeInLine(models.Model):
    _name = "estate.property.type.inline"
    _description = "Estate Property Type Inline"

    name = fields.Char(
        required=True,
    )
    