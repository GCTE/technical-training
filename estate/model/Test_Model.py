from odoo import models, fields, tools, api

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    active = fields.Boolean(
        default=True
    )
    name = fields.Char(
        required=True, 
        index=True
    )
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False,
        default=fields.Date.add(
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
    garden_orientation = fields.Selection(
        string='GardenOrientationCustomLabel',
        selection=[('north','North'), ('south','South'), ('east' ,'East'), ('west','West')],
        help='Is this a tooltip?'
    )
