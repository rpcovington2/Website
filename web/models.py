from web.app import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_login import UserMixin


class SignUpForm(FlaskForm):
    FirstName = StringField('First Name', [DataRequired()])
    LastName = StringField('Last Name', [DataRequired()])
    Email = StringField('E-Mail Address', [DataRequired()])
    Password = PasswordField('Password', [DataRequired(), Length(min=4, max=20)])
    Password2 = PasswordField('Confirm Password', [DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    Email = StringField('E-Mail Address', [DataRequired()])
    Password = StringField('Password', [DataRequired()])
    submit = SubmitField('Submit')


class EditProfile(FlaskForm):
    FirstName = StringField('First Name')
    LastName = StringField('Last Name')
    Email = StringField('E-Mail Address')
    HomePhone = StringField('Phone')
    MobilePhone = StringField('Mobile')
    Address = StringField('Address')
    City = StringField('City')
    State = StringField('State')
    submit = SubmitField('Submit')


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(45), index=False, unique=True, nullable=False)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    Email = db.Column(db.String(255))
    PasswordHash = db.Column(db.String(45))


class Info(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    Email = db.Column(db.String(255))
    Phone = db.Column(db.String(80))
    Mobile = db.Column(db.String(80))
    Address = db.Column(db.String(80))
    City = db.Column(db.String(80))
    State = db.Column(db.String(80))
    Title = db.Column(db.String(80))


class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    StartDate = db.Column(db.String(80))
    EndDate = db.Column(db.String(255))
