from odoo import models, fields, api


class CustomGroups(models.Model):
    _name = 'custom_setting.custom_groups'

    name = fields.Char(string="Group Name")
    comment = fields.Char()
    regular_emp = fields.Boolean(string="Regular user, the user will be able to manage his own human resources stuff"
                                        " (leave request, time sheets, ...).")
    emp_officer = fields.Boolean(string='Employee officer, the user will be able to approve'
                                        ' document created by employees.')
    emp_manger = fields.Boolean(string='Employee manager, the user will all rights to the human resources configuration '
                                       'as well as statistic reports.')
    payroll_officer = fields.Boolean(string='Pay roll officer, This user can generate payslips, salary structure,'
                                            ' contribution register and salary rule category.')
    payroll_manager = fields.Boolean(string='Pay roll manager, Has all rights of payroll officer.'
                                            ' This user can access workdays(read, create, delete, update).'
                                            ' He can also  generate payslips and edit salary'
                                            ' rules inputs. Has all rights of payroll officer.')
    fleet_user = fields.Boolean(string='Fleet user, This user can only see his vehicle details'
                                       ' and create and edit fuel and odometer logs.')
    fleet_manager = fields.Boolean(string='Fleet manager, This user has all rights on fleet management.')
    attendance_officer = fields.Boolean(string='Attendance officer,this user can access all users attendance.')
    attendance_manger = fields.Boolean(string='Has all rights of attendance officer and access manual attendance.')
    leaves_officer = fields.Boolean(string='Leaves officer,This user can access leaves, attendance info and events.')
    leaves_manger = fields.Boolean(string='Has all rights of leaves officer. this user can set'
                                          ' leaves types and meeting types.')
    def fun(self):
        print (self.env.uid)
