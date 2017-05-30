from odoo import models, fields, api
import datetime


class Relatives(models.Model):
    _name = 'custom_employee.relatives'

    name = fields.Char(string='Name')
    dateOfBirth = fields.Date(string="Date Of Birth")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')])
    age = fields.Char(compute='calc_age')
    type_id = fields.Many2one('custom_employee.relation_type')
    employee_id = fields.Many2one('hr.employee')

    @api.onchange('dateOfBirth')
    def calc_age(self):
        for data in self:
            if data.dateOfBirth:
                current_year = datetime.datetime.now().year
                birth_year = datetime.datetime.strptime(data.dateOfBirth, "%Y-%m-%d").year
                age = current_year - birth_year
                data.age = age

    @api.onchange("gender")
    def onchange_gender(self):
        print ('called')
        domain = []
        if self.gender == 'm':
            domain = [('id', 'in', [1, 2, 3])]
            print ("called male")
        elif self.gender == 'f':
            domain = [('id', 'not in', [1, 2, 3])]
            print ("called female")
        return {'domain': {'type_id': domain}}

    @api.depends("type_id")
    def onchange_type(self):
        print ("change")
        domain = []
        if self.gender == 'm':
            domain = [('id', 'in', [1, 2, 3])]
            print ("change to male")
        elif self.gender == 'f':
            domain = [('id', 'not in', [1, 2, 3])]
            print ("change to female")
        return {'domain': {'type_id': domain}}
