from forms import AddEnrolled, AddFacultyForm
import os
from forms import AddForm, DelForm, AddClass,AddEnrolled,AddFacultyForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "databaseProject"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_keys=True)
    name = db.Column(db.Text)
    major = db.Column(db.Integer,primary_keys=True)
    level = db.Column(db.Integer,primary_keys=True)
    age = db.Column(db.Integer,primary_keys=True)

    def __init__(self, name):
        self.name = name

class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_keys=True)
    name = db.Column(db.Text)
    dept_id = db.Column(db.Integer, primary_keys=True)

    def __init__(self, name):
        self.name = name
    
class Classes(db.Model):
    __tablename__ = 'Classes'
    name = db.Column(db.Text)
    meet_at = db.Column(db.Integer, primary_keys=True)
    Room = db.Column(db.Text)
    id = db.Column(db.Integer, primary_keys=True)

    def __init__(self, name):
        self.name = name

class Enrolled(db.Model):
    __tablename__ = 'Enrolled'
    id = db.Column(db.Integer, primary_keys=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_faculty',methods=['GET','POST'])
def add_faculty():
    form = AddFacultyForm()
    if form.validate_on_submit():
        name = form.name.data
        dept_id = form.dept_id.data
        new_faculty = Faculty(name, dept_id)
        db.session.add(new_faculty)
        db.session.commit()
        return redirect(url_for('list_student'))
    return render_template('add_faculty.html', form=form)


@app.route('/add_enrolled',methods=['GET','POST'])
def add_faculty():
    form = AddEnrolled
    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        new_enrolled = Enrolled(name, id)
        db.session.add(new_enrolled)
        db.session.commit()
        return redirect(url_for('list_student'))
    return render_template('add_enrolled.html', form=form)



@app.route('/add_class',methods=['GET','POST'])
def add_faculty():
    form = AddClass
    if form.validate_on_submit():
        name = form.name.data
        meet_at = form.meet_at.data
        Room = form.Room.data
        id = form.id.data
        new_enrolled = Enrolled(name, id)
        db.session.add(new_enrolled)
        db.session.commit()
        return redirect(url_for('list_student'))
    return render_template('add_enrolled.html', form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_student = Student(name)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('list_student'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_student():
    students = Student.query.all()
    return render_template('list.html', students=students)


@app.route('/delete', methods=['GET', 'POST'])
def del_student():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('list_student'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)