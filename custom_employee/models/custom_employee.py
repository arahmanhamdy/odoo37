from odoo import models, fields


class EmployeeTemplateInherete(models.Model):
    _inherit = 'hr.employee'
    relatives_ids = fields.One2many('custom_employee.relatives', 'employee_id')
    certificates_ids = fields.One2many('custom_employee.certificates', 'employee_id')