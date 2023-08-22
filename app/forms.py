from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
	email = EmailField('Email Address: password: ', validators=[DataRequired()])
	password = PasswordField('Password: ', validators=[DataRequired()])
	submit_btn = SubmitField('Sign In')


class SignupForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])
	confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit_btn = SubmitField('Register')
