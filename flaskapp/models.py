from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True, nullable=False)
    teacher = db.Column(db.String(64), nullable=False)
    assignments = db.relationship('Assignment', backref='course', lazy=True)
    lectures = db.relationship('Lecture', backref='course', lazy=True)
    
    def __repr__(self):
        return f"Course('{self.name}', '{self.teacher}')"


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    week = db.Column(db.Integer, nullable=False)
    date_due = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    upload_file = db.Column(db.String(32), nullable=False, default='def_ass.pdf')
    class_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    
    def __repr__(self):
        return f"Assignment('{self.name}', '{self.upload_file}', '{self.course.name}')"


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    week = db.Column(db.Integer, nullable=False)
    upload_file = db.Column(db.String(32), nullable=False, default='def_lec.pdf')
    class_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    
    def __repr__(self):
        return f"Assignment('{self.name}', '{self.upload_file}')"

