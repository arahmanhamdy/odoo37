from odoo import models, fields, api


class Training(models.Model):
    _name = 'custom_employee.training'

    name = fields.Char()
    department_ids = fields.Many2many('hr.department', string='Department')
    employee_ids = fields.Many2many('hr.employee', string='Trainees')
    employees_dept = []
    # employee_job_id = fields.Many2one('hr.job', string='Job Title')
    training_provider_id = fields.Many2one('custom_employee.training_provider', string='Training provider')
    location = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    status = fields.Selection([('s', 'started'), ('c', 'canceled'), ('p','postponed'), ('f','finished')])

    @api.multi
    def depts_ids(self):
        dept_ids = []
        if self.department_ids:
            for dept in self.department_ids:
                for emp in dept.member_ids:
                    dept_ids.append(emp.id)
        return dept_ids

    @api.onchange("department_ids")
    def get_employees(self):
        print ("new emp")
        domain = [('id', 'in', self.depts_ids())]
        return {'domain': {'employee_ids': domain}}


