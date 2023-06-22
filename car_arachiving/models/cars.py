from odoo import models, fields

class CarArchive(models.Model):
    _name = 'car.archive'
    _description = 'Car Archive'

    name = fields.Char(string='Car Name', required=True)
    make = fields.Char(string='Make', required=True)
    model = fields.Char(string='Model', required=True)
    year = fields.Integer(string='Year', required=True)
    color = fields.Char(string='Color')
    registration_number = fields.Char(string='Registration Number')
    owner_name = fields.Char(string='Owner Name')
    owner_address = fields.Char(string='Owner Address')
    date_added = fields.Datetime(string='Date Added', default=fields.Datetime.now)
    active = fields.Boolean(string='Active', default=True)