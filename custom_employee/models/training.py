from odoo import models, fields


class Training(models.Model):
    _name = 'custom_employee.training'

    name = fields.Char()
    department_ids = fields.Many2many('hr.department', string='Department')
    employee_id = fields.Many2one('hr.employee', string='Trainee')
    employee_job_id = fields.Many2one('hr.job', string='Job Title')
    training_provider_id = fields.Many2one('custom_employee.training_provider', string='Training provider')
    location = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    status = fields.Selection([('s', 'started'), ('c', 'canceled'), ('p','postponed'), ('f','finished')])