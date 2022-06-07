from . import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    FirstName = StringField('First Name', [DataRequired()])
    LastName = StringField('Last Name', [DataRequired()])
    Email = StringField('E-Mail Address', [DataRequired()])
    Password = StringField('Password', [DataRequired()])
    Password2 = StringField('Confirm Password', [DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    Email = StringField('E-Mail Address', [DataRequired()])
    Password = StringField('Password', [DataRequired()])
    submit = SubmitField('Submit')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(45), index=False, unique=True, nullable=False)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    Email = db.Column(db.String(255))
    PasswordHash = db.Column(db.String(45))
