from odoo import models, fields, tools, api

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        copy=False
    )
    property_id = fields.Many2one("estate.property", required=True)
    partner_id = fields.Many2one("res.partner", required=True)
    validity = fields.Integer(
        default=7,
        string="Validity (days)"
    )
    date_deadline = fields.Date(
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        search="_search_date_deadline",
        store=True,
        string="Deadline"
    )

    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.validity:
                offer.date_deadline = fields.Date.add(fields.Date.today(), days=offer.validity)
            else:
                offer.date_deadline = False
    
    @api.depends('date_deadline')
    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                offer.validity = (offer.date_deadline - fields.Date.today()).days
            else:
                offer.validity = 0

    def _search_date_deadline(self, operator, value):
        if operator not in ('=', '!=', '<', '<=', '>', '>='):
            raise ValueError("Invalid search operator for date_deadline")
        target_date = fields.Date.to_date(value)
        offers = self.search([])
        matching_offers = offers.filtered(lambda o: o.date_deadline and self._compare_dates(o.date_deadline, operator, target_date))
        return [('id', 'in', matching_offers.ids)]