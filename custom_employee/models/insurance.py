from odoo import models, fields


class Insurance(models.Model):
    _name = 'custom_employee.insurances'
    name = fields.Char(string='Name')