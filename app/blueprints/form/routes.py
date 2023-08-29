#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import requests
from flask import render_template, jsonify
from marshmallow import Schema, fields, EXCLUDE

from . import form


class CardSchema(Schema):
    abilities = fields.List(fields.Dict(), allow_none=True)
    artist = fields.Str(allow_none=True)
    ancientTrait = fields.Str(allow_none=True)
    attacks = fields.List(fields.Dict(), allow_none=True)
    convertedRetreatCost = fields.Int(allow_none=True)
    evolvesFrom = fields.Str(allow_none=True)
    flavorText = fields.Str(allow_none=True)
    hp = fields.Str(allow_none=False)
    id = fields.Str(allow_none=True)
    images = fields.Dict(allow_none=True)
    legalities = fields.Dict(allow_none=True)
    regulationMark = fields.Str(allow_none=True)
    name = fields.Str(allow_none=True)
    nationalPokedexNumbers = fields.List(fields.Int(), allow_none=True)
    number = fields.Str(allow_none=True)
    rarity = fields.Str(allow_none=True)
    resistances = fields.List(fields.Dict(), allow_none=True)
    retreatCost = fields.List(fields.Str(), allow_none=True)
    rules = fields.List(fields.Str(), allow_none=True)
    set = fields.Dict(allow_none=True)
    subtypes = fields.List(fields.Str(), allow_none=True)
    supertype = fields.Str(allow_none=True)
    tcgplayer = fields.Dict(allow_none=True)
    types = fields.List(fields.Str(), allow_none=True)
    weaknesses = fields.List(fields.Dict(), allow_none=True)

    class Meta:
        unknown = EXCLUDE


def fetch_card_data(name):
    url = f"https://api.pokemontcg.io/v2/cards?q=name:{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return jsonify({"error": "Card not found"}), 404


@form.route("/pokedex")
def pokedex():
    return render_template("pokedex.html")


@form.route("/api/card/<name>")
def get_card(name):
    card_data = fetch_card_data(name)

    if card_data:
        card_schema = CardSchema()
        card = card_schema.load(card_data, unknown=EXCLUDE)
        return jsonify(card)

    return jsonify({"error": "Card not found"}), 404
