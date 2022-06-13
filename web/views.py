from flask import Blueprint, render_template, url_for, redirect

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("index.html")


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


@views.route("/item")
def item():
    return render_template("item.html")


@views.route("/shop/<item>")
def id(item):
    print(item)
    return render_template("item.html")


@views.route("/pricing")
def princing():

    return render_template("price.html")
