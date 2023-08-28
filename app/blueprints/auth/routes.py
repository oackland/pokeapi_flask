#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
from flask import flash, redirect, url_for
from flask import render_template, request
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from app.models import User, db
from . import auth
from .forms import LoginForm, SignupForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		queried_user = User.query.filter(User.email == email).first()
		if queried_user and check_password_hash(queried_user.password, password):
			login_user(queried_user)
			flash(f'Welcome back {queried_user.first_name}!', 'primary')
			return redirect(url_for('pokemon.game'))
		else:
			flash('Invalid email or password', 'danger')
			return redirect(url_for('pokemon.home'))
	else:
		return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST' and form.validate_on_submit():
		first_name = form.first_name.data
		last_name = form.last_name.data
		email = form.email.data.lower()
		password = form.password.data
		new_user = User(first_name, last_name, email, password)

		db.session.add(new_user)
		db.session.commit()
		flash(f'Thank you for been a user {new_user.first_name}!', 'primary')
		return redirect(url_for('auth.login'))

	else:
		return render_template('signup.html', form=form)


@auth.route('/logout')
def logout():
	logout_user()
	return render_template('index.html')
