from odoo import models, fields

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    property_type_id = fields.Many2one(
        string="Property Type"
    )
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.users", string="Seller")
