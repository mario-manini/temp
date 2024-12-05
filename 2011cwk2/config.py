import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Flask-WTF configuration

WTF_CSRF_ENABLED = True
SECRET_KEY = 'a-very-secret-secret'