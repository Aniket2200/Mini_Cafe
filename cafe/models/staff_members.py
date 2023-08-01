from odoo import fields, models,api,_
import re
from odoo.exceptions import ValidationError

class StaffMember(models.Model):
    _name = 'cafe.staff_member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Cafe Staff Member'
    _rec_name = "name"

    name = fields.Char(string='Name', required=True, tracking=True)
    cell_no = fields.Char(string = "Phone Number", required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    address = fields.Text(string="Address", tracking=True)
    active = fields.Boolean(default='False', selection=[(True, 'Enabled'), (False, 'Disabled')])
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)


    # Email validations
    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email and not self._is_valid_email(record.email):
                raise ValidationError('Invalid email format')
    def _is_valid_email(self, email):
        import re
        pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        return re.match(pattern, email)

    @api.constrains('cell_no')
    def _validate_contact(self):
        for record in self:
            if record.cell_no:
                pattern = r'^[789]\d{9}$'
                if not re.match(pattern, record.cell_no):
                    raise models.ValidationError('Invalid patient contact number!')




    #Below Reference Code
    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('cafe.staff_member') or _('New')
        res = super(StaffMember, self).create(vals)
        return res
