from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeTemplateInherete(models.Model):
    _inherit = 'hr.employee'
    relatives_ids = fields.One2many('custom_employee.relatives', 'employee_id')
    certificates_ids = fields.One2many('custom_employee.certificates', 'employee_id')
    educations_ids = fields.Many2many('custom_employee.educations')
    insurances_ids = fields.Many2many('custom_employee.insurances',string='Insurance')
    car_id = fields.Many2one('fleet.vehicle', string='Car')