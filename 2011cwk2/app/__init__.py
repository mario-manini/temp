from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, login_user, current_user

app = Flask(__name__)
app.config.from_object('config')

#initialize database, migrate and bcrypt
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)


#create database
with app.app_context():
    db.create_all()


from . import views

