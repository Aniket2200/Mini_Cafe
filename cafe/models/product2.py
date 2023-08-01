from odoo import models, fields, api


class Product2(models.Model):
    _name = 'cafe.starter'
    _description = 'Product Data '

    name = fields.Char(string='Product Name')
