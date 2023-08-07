from odoo import models, fields

class User(models.Model):
    _name = 'my_user_module.user'
    _description = 'User Information'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)
    # Add any additional fields you need for user information
