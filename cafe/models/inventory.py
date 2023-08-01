from odoo import models, fields


class StaffMember(models.Model):
    _name = 'cafe.inventory'
    _description = 'Cafe Inventory'
    _rec_name = "table_no"


    table_no = fields.Char(string='Table No', copy=False)
    capacity = fields.Integer(string='Capacity')



    _sql_constraints = [
        ('table_no', 'UNIQUE(table_no)', 'This Table No already added...!!!')
    ]


