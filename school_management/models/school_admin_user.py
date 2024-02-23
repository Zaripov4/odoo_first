from odoo import models, fields, api

class AdminUser(models.Model):
    _name = 'school.admin.user'
    _description = 'Admin User'

    admin_id = fields.Many2one('school.admin', string='Admin')
    user_id = fields.Many2one('res.users', string='User')

    @api.model
    def create(self, vals):
        user = self.env['res.users'].create({
            'name': vals.get('name'),
            'login': vals.get('login'),
            'password': vals.get('password')
        })
        vals['user_id'] = user.id
        return super(AdminUser, self).create(vals)
