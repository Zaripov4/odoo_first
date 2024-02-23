from odoo import models, fields

class Course(models.Model):
    _name = "school.course"
    _description = "Courses"

    name = fields.Char(string="Name")
    teacher_id = fields.Many2one("school.teacher", string="Teacher")
    student_ids = fields.Many2many("school.student", string="Students")
