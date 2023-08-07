from odoo import fields, models

class PunchManagement(models.Model):
    _name = 'punch.management'

    user_id = fields.Many2one('user.management', string='User')
    punch_date = fields.Date(default=fields.Date.today, string='Date')
    punch_type = fields.Selection([('punch_in', 'Punch In'), ('punch_out', 'Punch Out')], string='Punch Type')