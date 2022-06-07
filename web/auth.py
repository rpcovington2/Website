from flask import Blueprint, render_template, flash, redirect, url_for
from .models import SignUpForm, User, LoginForm
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    total = User.query.all()
    print(total)
    loginform = LoginForm()
    if loginform.validate_on_submit():
        users = User.query.filter(User.Email == loginform.Email.data).count()
        print(users)
        if users == 1:
            checkPassword = User.query.filter(User.Email == loginform.Email.data).all()
            for x in checkPassword:
                if x.PasswordHash == loginform.Password.data:
                    flash("Login Successful!!", 'Success')
                    return redirect(url_for('views.home'))
        else:
            flash("Sign up Here", 'error')

    return render_template("Login.html", loginform=loginform)


@auth.route("/logout")
def logout():
    return render_template("home.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():

    form = SignUpForm()
    if form.validate_on_submit():

        Email = form.Email.data
        users = User.query.filter(User.Email == Email).count()
        if users >= 1:
            flash("Email Already in use!!!", 'error')
        else:
            userCount = User.query.count()
            if form.Password.data == form.Password2.data:
                new_User = User(id=int(userCount) + 1,
                                FirstName=form.FirstName.data,
                                LastName=form.LastName.data,
                                Email=form.Email.data,
                                PasswordHash=form.Password.data,
                                )
                db.session.add(new_User)
                db.session.commit()
                flash("Account Created!!", "Success")
                print(f"First Name: {form.FirstName.data}")
                print(f"Last name: {form.LastName.data}")
                print(f"E-Mail: {form.Email.data}")
                print(f"Password: {form.Password.data}")
                print(f"Confirm Password: {form.Password2.data}")
                return redirect(url_for('views.home'))
            else:
                flash("Passwords Do not Match!!!", "error")

    return render_template("SignUp.html", form=form)
