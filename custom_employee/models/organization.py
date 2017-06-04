from odoo import models, fields, api
import json


class DepartTemplateInherit(models.Model):
    _inherit = 'hr.department'

    type = fields.Many2one('custom_employee.unit_type','Type')

