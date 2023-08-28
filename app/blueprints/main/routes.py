# import requests
import requests
from flask import Blueprint, render_template, request
from flask_login import login_required


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/index")
def home():
    return 'home'


@main.route("/projects")
def projects():
    return render_template("projects.html")


@main.route("/contact")
def contacts():
    return render_template("contacts.html")


@main.route("/game")
@login_required
def game():
    return render_template("game.html", pokemon_data=None, error_message=None)


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


# from here is test
@main.route("/battle")
def battle():
    return render_template("battle.html")

#
# character_choices = {
#     "male": ["Ash", "Brock", "Red"],
#     "female": ["Misty", "May", "Leaf"],
# }
#
# team_choices = {
#     "Ash": ["Team Rocket", "Team Valor", "Team Mystic"],
#     "Brock": ["Team Instinct", "Team Mystic", "Team Galactic"],
#     "Red": ["Team Rocket", "Team Aqua", "Team Magma"],
#     "Misty": ["Team Valor", "Team Instinct", "Team Rocket"],
#     "May": ["Team Mystic", "Team Instinct", "Team Aqua"],
#     "Leaf": ["Team Instinct", "Team Valor", "Team Galactic"],
# }
#
#
# @main.route("/pokemon", methods=["GET", "POST"])
# def pokemon():
#     if request.method == "POST":
#         gender = request.form.get("gender")
#         character = request.form.get("character")
#         team = request.form.get("team")
#         pokemon = request.form.get("pokemon")
#
#         return render_template(
#             "index.html",
#             character_choices=character_choices[gender],
#             team_choices=team_choices[character],
#             selected_character=character,
#             selected_team=team,
#             selected_pokemon=pokemon,
#         )
#
#     return render_template(
#         "landing.html", genders=["male", "female"], team_choices=team_choices
#     )
#
#
# @main.route("/pokemon", methods=["GET", "POST"])
# def pokemon():
#     if database_is_populated():
#         return redirect(url_for("pokemon"))  # Redirect to the character selection page
#
#     if request.method == "POST":
#         gender = request.form.get("gender")
#         # ... handle other form submissions ...
#
#     return render_template("index.html", genders=["male", "female"])
#
