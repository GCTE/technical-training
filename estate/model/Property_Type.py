from odoo import models, fields

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

    property_type_id = fields.Many2one(
        string="Property Type"
    )
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.partner", string="Seller")
