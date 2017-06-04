from odoo import models, fields


class Vehicle(models.Model):

    _inherit = 'fleet.vehicle'
    employee_id = fields.many2one('hr.employee','Employee')