#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
from flask import render_template

from . import pokemon
from .pokemonClass import Pokemonclass


@pokemon.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    card = Pokemonclass.get_card_by_name("Pikachu")  # Replace "Pikachu" with user input
    img_url = card.get("images", {}).get(
        "small"
    )  # Adjust based on the actual API response
    return render_template("pokemon.html", img_url=img_url)
