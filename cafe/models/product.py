from odoo import models, fields, api


class Product1(models.Model):
    _name = 'cafe.drink'
    _description = 'Product Data '

    name = fields.Char(string='Product Name')


