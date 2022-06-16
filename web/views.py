from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from web.models import SignUpForm, User, LoginForm
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
    return render_template("Profile.html", user=current_user)


@views.route("/events")
def events():
    return render_template("Events.html", user=current_user)


@views.route("/projects")
def projects():
    return render_template("Projects.html", user=current_user)


@views.route("/shop")
def Shop():
    return render_template("Shop.html", user=current_user)


@views.route("/item")
def item():
    return render_template("item.html")


@views.route("/shop/<item>")
def id(item):
    print(item)
    return render_template("item.html")


@views.route("/pricing")
def pricing():

    return render_template("price.html")


@views.route("/learn")
def learn():

    return render_template("learn.html")
