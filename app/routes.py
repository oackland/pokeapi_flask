from flask import Blueprint, render_template, request
import requests

bp = Blueprint("pokemon", __name__)


@bp.route("/")
def index():
	return render_template("index.html", pokemon_data=None, error_message=None)


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

		return render_template("index.html", pokemon_data=pokemon_data, error_message=None)

	except requests.exceptions.RequestException as e:
		error_message = f"Error fetching Pokémon data: {str(e)}"
		return render_template("index.html", pokemon_data=None, error_message=error_message)
