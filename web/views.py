from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("Home.html")


@views.route("/profile")
def profile():
    return render_template("Profile.html")


@views.route("/events")
def events():
    return render_template("Events.html")


@views.route("/projects")
def projects():
    return render_template("Projects.html")

@views.route("/shop")
def Shop():
    return render_template("Shop.html")
