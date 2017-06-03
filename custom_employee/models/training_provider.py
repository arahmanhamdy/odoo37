from odoo import models, fields


class TrainingProvider(models.Model):
    _name = 'custom_employee.training_provider'
    name = fields.Char()
    adress = fields.Text()
    phone_number = fields.Char()