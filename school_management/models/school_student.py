from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Students'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    course_ids = fields.Many2many('school.course', string='Courses')
