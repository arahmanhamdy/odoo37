from odoo import models, fields


class UnitType(models.Model):
    _name = 'custom_employee.unit_type'

    name = fields.Char(string='Name')

