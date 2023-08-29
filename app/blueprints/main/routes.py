#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import requests
from flask import render_template, request, app
from flask_login import login_required

from . import main


@main.route("/")
@main.route("/index")
def home():
    return render_template("index.html")


@main.route("/signup")
def signup():
    return render_template("signup.html")


@main.route("/game")
@login_required
def game():
    return render_template("game.html", pokemon_data="pikachu", error_message=None)


@main.route("/fetch_pokemon_data", methods=["POST"])
def fetch_pokemon_data():
    try:
        pokemon_name = request.form.get("pokemonName")

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
        response.raise_for_status()
        data = response.json()

        pokemon_data = {
            "name": data["name"],
            "hp": data["stats"][0]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "sprite_url": data["sprites"]["front_shiny"],
            "ability": data["abilities"][0]["ability"]["name"],
        }

        return render_template(
            "game.html", pokemon_data=pokemon_data, error_message=None
        )

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching Pokémon data: {str(e)}"
        return render_template(
            "game.html", pokemon_data=None, error_message=error_message
        )


if __name__ == "__main__":
    app.run()
