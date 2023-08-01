from odoo import models, fields, api,_
class Order(models.Model):
    _name = 'cafe.order'
    _description = 'Cafe Order'
    _order = 'date_time desc'

    staff_ids = fields.Many2one('cafe.staff_member', string="Staff")
    refer = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    table_ids = fields.Many2one('cafe.inventory', string='Dine In')
    category_id = fields.Many2one('cafe.category', string='Category Name')
    date_time = fields.Datetime(string='Date And Time', default=fields.Datetime.now(), required=True)
    product_name = fields.Many2one('cafe.main', string="Product Name")
    subtotal = fields.Float(compute='_compute_subtotal', string='Sub Total')
    subtotal2 = fields.Float(related='order_line_ids.sub_total1')
    total_amount = fields.Float(compute='_compute_total', string='Grand Total')

    order_line_ids = fields.One2many('cafe.order.line', 'order_id', string='Product Line')

    state = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], default="unpaid", string="Payment", tracking=True)

    # @api.multi
    # def print_report(self):
    #     return self.env.ref(cafe.report_order_card) .report_action(self)

    def action_unpaid(self):
        self.state = 'unpaid'

    def action_paid(self):
        self.state = 'paid'

    @api.depends('order_line_ids.price', 'order_line_ids.quantity')
    def _compute_subtotal(self):
        for purchase in self:
            purchase.subtotal = sum((line.price * line.quantity) for line in purchase.order_line_ids)

    @api.depends('subtotal', 'subtotal2')
    def _compute_total(self):
        for purchase in self:
            purchase.total_amount = purchase.subtotal

    @api.model
    def create(self, vals):
        if vals.get('refer', _('New')) == _('New'):
            vals['refer'] = self.env['ir.sequence'].next_by_code('cafe.order') or _('New')
        res = super(Order, self).create(vals)
        return res

class Order_line(models.Model):
    _name = 'cafe.order.line'
    _description = 'Cafe Order Line'

    product_name = fields.Many2one('cafe.main', string="Product Name")
    category_name = fields.Many2one(related='product_name.category_id', string="Category Name")
    order_id = fields.Many2one('cafe.order', string='Order Name')
    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(related='product_name.price', string='Price')
    sub_total1 = fields.Float(string='Sub Total', compute='_compute_subtotal')

    @api.depends('price', 'quantity')
    def _compute_subtotal(self):
        for order in self:
            order.sub_total1 = order.price * order.quantity

    # products = fields.Char(string="product name")
    # drink = fields.Boolean(string="Drink")
    # starter = fields.Boolean(string="Starter")
    # product_id1 = fields.Many2one('cafe.drink', string="Product Name")
    # product_id2 = fields.Many2one('cafe.starter', string="Product Name")



