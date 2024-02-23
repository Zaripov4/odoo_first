from odoo import models, fields

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teachers"

    name = fields.Char(string="Name")
    salary = fields.Float(string="Salary")
    course_ids = fields.One2many("school.course", "teacher_id", string="Courses")
