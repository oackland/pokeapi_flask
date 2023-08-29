#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

# # your task is to create a class to get the card by a name,
# # type, rarity and description.
# # Also need to get the battlefield points meaning you will
# # need to get power, defense and attack
#
# # then display the card to the user in html using stats table
# # max card sport is 5 and minimum is 0
# # now you need to provide the available number to the user
#
# "get me an idea for the card"
#
#
# # class card:
# #     def __init__(self, name, poke_type, rarity, description):
# #         self.name = name
# #         self.poke_type = poke_type
# #         self.rarity = rarity
# #         self.description = description
# #
# #     def __str__(self):
# #         return f"Name: {self.name}\nType: {self.poke_type}\nRarity: {self.rarity}\nDescription: {self.description}"
# #
# #     def __repr__(self):
# #         return self.poke_type
# #
# #     def __eq__(self, other):
# #         return self.name == other.name
# #
# #     def __ne__(self, other):
# #         return self.name != other.name
# #
# #     def __hash__(self):
# #         return hash(self.name)
# #
# #
# # # Create some sample Pokémon cards for demonstration
# # card1 = card(
# #     "Pikachu",
# #     "Electric",
# #     "Common",
# #     "A famous Pokémon known for its thunderbolt attack.",
# # )
# # card2 = card(
# #     "Charizard", "Fire", "Rare", "A dragon-like Pokémon that can breathe fire."
# # )
# # card3 = card(
# #     "Bulbasaur", "Grass", "Uncommon", "A Pokémon that has a plant seed on its back."
# # )
# #
# # # Store them in a dictionary for easy lookup using their names
# # pokecards = {card1.name: card1, card2.name: card2, card3.name: card3}
# #
# # # Ask the user for a Pokémon name
# # pokemon_name = input("Enter the name of the Pokémon: ")
# #
# # # Lookup and print the card details, if it exists in our collection
# # if pokemon_name in pokecards:
# #     print(pokecards[pokemon_name])
# # else:
# #     print("Sorry, we don't have that Pokémon card.")
#
# #
# # # how to retrieve data from API
# #
# # # 1. pip install requests. import requests
# # import requests
# #
# # response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
# # response.raise_for_status()
# # data = response.json()
# # pokemon_data = {
# #     "name": data["id"],
# # }
# # print(pokemon_data)
#
#
# import requests
# from marshmallow import Schema, fields
#
#
# class CardSchema(Schema):
#     id = fields.Str()
#     name = fields.Str()
#     types = fields.List(fields.Str())
#     rarity = fields.Str()
#     flavorText = fields.Str()
#
#
# def fetch_card_data(name):
#     url = f"https://api.pokemontcg.io/v2/cards?q=name:{name}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
#
#
# card_data = fetch_card_data("pikachu")
# if card_data:
#     cards = card_data.get("data", [])
#     if cards:
#         # Assuming you want the first card that matches the name "Gardevoir"
#         card_schema = CardSchema()
#         card = card_schema.load(cards[0], unknown="EXCLUDE")
#
#         print(card)
#     else:
#         print("No cards found")
# else:
#     print("Error fetching card data")
#
# import requests
# from marshmallow import Schema, fields, EXCLUDE
#
#
# class CardSchema(Schema):
#     id = fields.Str()
#     name = fields.Str()
#     types = fields.List(fields.Str(), allow_none=True)
#     rarity = fields.Str(allow_none=True)
#     flavorText = fields.Str(allow_none=True)
#
#     class Meta:
#         unknown = EXCLUDE
#
#
# def fetch_card_data(name):
#     url = f"https://api.pokemontcg.io/v2/cards?q=name:{name}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
#
#
# card_data = fetch_card_data("Gardevoir")
# print("API response: ", card_data)  # Just to inspect the API response
#
# if card_data:
#     cards = card_data.get("data", [])
#     if cards:
#         card_schema = CardSchema()
#         card = card_schema.load(cards[0], unknown=EXCLUDE)
#         print("Deserialized card: ", card)
