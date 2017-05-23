from odoo import models, fields


class RelationType(models.Model):
    _name = 'custom_employee.relation_type'
    _rec_name = "type"

    type = fields.Char(string="type")
