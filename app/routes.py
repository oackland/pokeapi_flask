#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import requests
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from .forms import LoginForm, SignupForm
from .models import User, db

bp = Blueprint("pokemon", __name__)


# @bp.route('/post/<int:post_id>')
# def post(post_id):
# 	return f'This is post number {post_id}'
#

@bp.route('/')
@bp.route('/index')
def home():
	return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
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


@bp.route('/signup', methods=['GET', 'POST'])
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
		return redirect(url_for('pokemon.login'))

	else:
		return render_template('signup.html', form=form)


@bp.route('/logout')
def logout():
	logout_user()
	return render_template('index.html')


@bp.route("/projects")
def projects():
	return render_template("projects.html")


@bp.route("/contact")
@login_required
def contacts():
	return render_template("contacts.html")


# @bp.route("/signup")
# def signup():
# 	return render_template("signup.html")


@bp.route("/game")
@login_required
def game():
	return render_template("game.html", pokemon_data="pikachu", error_message=None)


@bp.route("/fetch_pokemon_data", methods=["POST"])
def fetch_pokemon_data():
	try:
		pokemon_name = request.form.get("pokemonName")

		response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
		response.raise_for_status()
		data = response.json()

		pokemon_data = {
				"name":       data["name"],
				"hp":         data["stats"][0]["base_stat"],
				"defense":    data["stats"][2]["base_stat"],
				"attack":     data["stats"][1]["base_stat"],
				"sprite_url": data["sprites"]["front_shiny"],
				"ability":    data["abilities"][0]["ability"]["name"]
		}

		return render_template("game.html", pokemon_data=pokemon_data, error_message=None)

	except requests.exceptions.RequestException as e:
		error_message = f"Error fetching Pokémon data: {str(e)}"
		return render_template("game.html", pokemon_data=None, error_message=error_message)


if __name__ == '__main__':
	app.run()
