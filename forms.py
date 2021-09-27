from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.core import TimeField

class AddForm(FlaskForm):
    id = IntegerField("Id of student is :")
    name = StringField("Name of Student: ")
    major = IntegerField("Enter student major: ")
    level = IntegerField("Enter student level: ")
    age = IntegerField("Age of student is :")
    submit = SubmitField("Add Student: ")

class AddClass(FlaskForm):
    name = StringField("Name of class")
    meet_at = IntegerField("Meet at")
    Room = StringField("Room : ")
    id = IntegerField("Class id is : ")

class DelForm(FlaskForm):
    id = IntegerField("Id of student is :")
    submit = SubmitField("Delete Data of Student: ")

class AddFacultyForm(FlaskForm):
    id = IntegerField("Id of Faculty is : ")
    name = StringField("Name of Student is : ")
    dept_id = IntegerField("Department Id : ")

class AddEnrolled(FlaskForm):
    id = IntegerField("Id of Enrolled : ")
    name = StringField("Name of Enrollment : ")
