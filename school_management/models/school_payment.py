from odoo import models, fields

class Payment(models.Model):
    _name = 'school.payment'
    _description = 'Payments'

    student_id = fields.Many2one('school.student', string='Student')
    amount = fields.Float(string='Amount')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
