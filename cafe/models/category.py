from odoo import models, fields


class Category(models.Model):
    _name = 'cafe.category'
    _description = 'Cafe Category'

    name = fields.Char(string='Category')

    _sql_constraints = [
        ('name', 'UNIQUE(name)', 'This Category already added...!!!')
    ]

