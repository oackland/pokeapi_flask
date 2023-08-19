from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/fetch_pokemon_data", methods=["POST"])
def fetch_pokemon_data():
	try:
		pokemon_name = request.form.get("pokemonName")

		response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
		response.raise_for_status()
		data = response.json()

		pokemon_data = {
				"name":            data["name"],
				"ability":         data["abilities"][0]["ability"]["name"],
				"base_experience": data["base_experience"],
				"sprite_url":      data["sprites"]["front_default"],
				"attack":          data["stats"][1]["base_stat"],
				"hp":              data["stats"][0]["base_stat"],
				"defense":         data["stats"][2]["base_stat"]
		}

		return jsonify(pokemon_data)

	except requests.exceptions.RequestException as e:
		error_message = f"Error fetching Pokémon data: {str(e)}"
		return jsonify({"error": error_message})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
