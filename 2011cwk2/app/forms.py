from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, ValidationError
from . import db


#make a form to get data about login and create user


class LoginForm(FlaskForm):
    username = StringField('ID',validators=[InputRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators=[InputRequired()])
    submit = SubmitField("Sign in")

class CreateAccountForm(FlaskForm):
    username = StringField('ID',validators=[InputRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators=[InputRequired()])
    submit = SubmitField("Register")