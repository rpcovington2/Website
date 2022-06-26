from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from web.models import *
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')

    return render_template("index.html", user=current_user, loginform=loginForm)


@views.route("/profile")
@login_required
def profile():

    info = Info.query.filter_by(Email=current_user.Email).first()

    EditProfileForm = EditProfile()

    if EditProfileForm.validate_on_submit():
        print(EditProfileForm.FirstName.data)
        print(EditProfileForm.LastName.data)
        print(EditProfileForm.MobilePhone.data)
        print(EditProfileForm.Address.data)
        print(EditProfileForm.City.data)
        print(EditProfileForm.State.data)
    return render_template("Profile.html", users=info, user=current_user, ProfileForm=EditProfileForm)


@views.route("/events")
def events():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')

    return render_template("Events.html", user=current_user, loginform=loginForm)


@views.route("/projects")
@login_required
def projects():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')



    return render_template("Projects.html", user=current_user, loginform=loginForm)


@views.route("/shop")
def Shop():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')
    return render_template("Shop.html", user=current_user, loginform=loginForm)


@views.route("/item")
def item():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')
    return render_template("item.html", user=current_user, loginform=loginForm)


@views.route("/shop/<item>")
def id(item):
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')
    return render_template("item.html", user=current_user, loginform=loginForm)


@views.route("/pricing")
def pricing():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')
    return render_template("price.html", user=current_user, loginform=loginForm)


@views.route("/learn")
def learn():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')

    return render_template("learn.html", user=current_user, loginform=loginForm)


def Login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        user = User.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.PasswordHash, loginForm.Password.data):
                login_user(user, remember=True)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            print("Error")
            flash("Sign up", 'error')

    return loginForm