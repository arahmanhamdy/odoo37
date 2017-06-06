from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeTemplateInherete(models.Model):

    # _name = 'custom_employee.employee'
    _inherit = 'hr.employee'
    relatives_ids = fields.One2many('custom_employee.relatives', 'employee_id')
    certificates_ids = fields.One2many('custom_employee.certificates', 'employee_id')
    educations_ids = fields.Many2many('custom_employee.educations')
    insurances_ids = fields.Many2many('custom_employee.insurances',string='Insurance')
    car_id = fields.Many2one('fleet.vehicle', string='Car')

#     def get_car(self):
#         record = self.env['fleet.vehicle'].search([])
#         print record
#
# e = EmployeeTemplateInherete()
# e.get_car()