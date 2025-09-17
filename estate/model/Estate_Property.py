from odoo import models, fields, tools, api
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(
        required=True, 
        index=True
    )
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=lambda self: fields.Date.add(
            fields.Date.today(), months=3
        )
    )
    expected_price = fields.Float()
    selling_price = fields.Float(
        readonly=True,
        copy=False
    )
    bedrooms = fields.Integer(
        default=2
    )
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_area_restore = fields.Integer()
    garden_orientation = fields.Selection(
        string='GardenOrientationCustomLabel',
        selection=[('north','North'), ('south','South'), ('east' ,'East'), ('west','West')],
        help='Is this a tooltip?'
    )
    garden_orientation_restore = fields.Selection(
        selection=[('north','North'), ('south','South'), ('east' ,'East'), ('west','West')],
        help='Is this a tooltip?'
    )
    active = fields.Boolean(
        default=True
    )
    state = fields.Selection(
        string='Status',
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        required=True,
        copy=False,
        default='new'
    )
    last_seen = fields.Datetime()

    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")

    total_area = fields.Float(
        readonly=True,
        compute="_compute_total_area"
    )

    best_price = fields.Float(
        readonly=True,
        compute="_compute_best_price"
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for property in self:
            if property.offer_ids:
                property.best_price = max(property.offer_ids.mapped('price'), default=0.0)
            else:
                property.best_price = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        for property in self:
            if not property.garden:
                #Store values from when unckecked?
                property.garden_area_restore = property.garden_area
                property.garden_area = 0
                property.garden_orientation_restore = property.garden_orientation
                property.garden_orientation = False
            else:
                if property.garden_area_restore:
                    property.garden_area = property.garden_area_restore
                if property.garden_orientation_restore:
                    property.garden_orientation = property.garden_orientation_restore

#<button name="action_cancel_property" type="object" string="Cancel Property"/>
    def action_cancel_property(self):
        for property in self:
            if property.state == 'sold':
                raise UserError("Sold properties cannot be cancelled.") 
            else:
                property.state = 'cancelled'
    
    def action_sold_property(self):
        for property in self:
            if property.state == 'cancelled':
                raise UserError("Cancelled properties cannot be sold.") 
            else:
                property.state = 'sold'