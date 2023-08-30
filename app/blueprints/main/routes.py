#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import requests
from flask import request, render_template
from flask_login import login_required

from . import main


#                                    ######################################
#                                    #####                              #####
#                                    ####           Home Page           ####
#                                    #####                              #####
#                                    ######################################


@main.route("/")
@main.route("/index")
def home():
    return render_template("index.html")


#                                    ######################################
#                                    #####                              #####
#                                    ####           Projects            ####
#                                    #####                              #####
#                                    ######################################


@main.route("/projects")
def projects():
    return render_template("projects.html")


#                                    ######################################
#                                    #####                              #####
#                                    ####        Pokemon game           ####
#                                    #####                              #####
#                                    ######################################


@main.route("/game")
@login_required
def game():
    return render_template("game.html", pokemon_data="pikachu", error_message=None)


#                                    ######################################
#                                    #####                              #####
#                                    ####           old card            ####
#                                    #####                              #####
#                                    ######################################


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


#                                    ######################################
#                                    #####                              #####
#                                    ####           pokemon card         ####
#                                    #####                              #####
#                                    ######################################


@main.route("/pokedex", methods=["GET", "POST"])
def pokedex():
    card_data = None
    if request.method == "POST":
        name = request.form.get("name")
        url = f"https://api.pokemontcg.io/v2/cards?q=name:{name}"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            if "data" in json_data and len(json_data["data"]) > 0:
                card_data = json_data["data"][0]
            else:
                card_data = "No card found"
    return render_template("pokedex.html", card=card_data)


#                                    ######################################
#                                    #####                              #####
#                                    ####       END OF SECTION           ####
#                                    #####                              #####
#                                    ######################################
#
# app = Flask(__name__)
# # app.secret_key = "s3cr3t"
#
#
# @poke.route("/pokedex", methods=["GET", "POST"])
# def pokedex():
#     if "cards" not in session:
#         session["cards"] = []
#
#     if request.method == "POST":
#         if "add" in request.form:
#             name = request.form.get("name")
#             if len(session["cards"]) < 5:
#                 card_data = Pokemonclass.get_card_by_name(name)
#                 if card_data:
#                     session["cards"].append(card_data)
#                     session.modified = True
#             else:
#                 return "Maximum 5 cards allowed", 400
#         elif "delete" in request.form:
#             card_id = request.form.get("delete")
#             session["cards"] = [
#                 card for card in session["cards"] if card["id"] != card_id
#             ]
#             session.modified = True
#
#     return render_template("pokedex.html", cards=session["cards"])
