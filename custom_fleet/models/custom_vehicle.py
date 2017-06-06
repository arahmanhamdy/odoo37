from odoo import models, fields, api


class Vehicle(models.Model):
    # _name = 'custom_fleet.vehicle'
    _inherit = 'fleet.vehicle'
    # employee_id = fields.Many2one('hr.employee', 'Employee')
    employee_id = fields.Char()
    # @api.onchange("employee_id")
    # def fun(self):
    #     print self.employee_id
