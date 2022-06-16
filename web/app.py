from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "makerspace"
app = Flask(__name__)


# def CreateApp():
# app = Flask(__name__)
app.config['SECRET_KEY'] = "ThisIStemporayUntilsetupinConfigFile"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://test:admin@127.0.0.1:3306/{DB_NAME}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

from .views import views
from .auth import auth

# createDatabase(app)

app.register_blueprint(views)
app.register_blueprint(auth)

# app.run()
from .models import User

loginManager = LoginManager()
loginManager.login_view = 'views.home'
loginManager.init_app(app)

@loginManager.user_loader
def loadUser(id):
    return User.query.get(int(id))


def createDatabase(app):
    if not path.exists("web/" + DB_NAME):
        db.create_all(app=app)
        print("Created DataBase!!")

