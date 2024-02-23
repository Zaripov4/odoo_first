from odoo import models, fields

class Admin(models.Model):
    _name = "school.admin"
    _description = "Admin"

    name = fields.Char(string="Name")
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")
