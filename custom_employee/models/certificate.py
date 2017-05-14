from odoo import models, fields ,api
import datetime


class Certificates(models.Model):
    _name = 'custom_employee.certificates'
    name = fields.Char(string='Name')
    certificate = fields.Binary(string='Certificate')
    employee_id = fields.Many2one('hr.employee')
