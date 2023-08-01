from odoo import models, fields


class MainInventory(models.Model):
    _name = 'cafe.main'
    _description = 'Cafe Main Inventory'
    _rec_name = "productname"


    category_id = fields.Many2one('cafe.category', string='Category Name')
    productname = fields.Char(string="Product Name")
    price = fields.Float(string="Price Per One Quantity")













