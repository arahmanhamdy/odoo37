from odoo import models, fields


class Educations(models.Model):
    _name = 'custom_employee.educations'
    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')