from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	email = EmailField('Email Address: password: ', validators=[DataRequired()])
	password = PasswordField('Password: ', validators=[DataRequired()])
	submit_btn = SubmitField('Sign In')
