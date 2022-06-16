from flask import Blueprint, render_template, flash, redirect, url_for
from web.models import SignUpForm, User, LoginForm
from web.app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        email = loginForm.Email.data
        users = User.query.filter_by(Email=email).first()
        if users:
            if check_password_hash(users.PasswordHash, loginForm.Password.data):
                login_user(users)
                flash("Login Successful!!", 'Success')
                return redirect(url_for('views.home'))
        else:
            flash("Sign up", 'error')

    return render_template("Login.html", loginform=loginForm)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route("/signup", methods=["GET", "POST"])
def signup():

    form = SignUpForm()
    if form.validate_on_submit():

        Email = form.Email.data
        users = User.query.filter(User.Email == Email).first()
        if users:
            flash("Email Already exists!!!", 'error')
        else:
            userCount = User.query.count()
            if form.Password.data == form.Password2.data:
                new_User = User(id=int(userCount) + 1,
                                FirstName=form.FirstName.data,
                                LastName=form.LastName.data,
                                Email=form.Email.data,
                                PasswordHash=generate_password_hash(form.Password.data),
                                )
                db.session.add(new_User)
                db.session.commit()
                flash("Account Created!!", "Success")
                login_user(users)
                return redirect(url_for('views.home'))
            else:
                flash("Passwords Do not Match!!!", "error")

    return render_template("SignUp.html", form=form)
