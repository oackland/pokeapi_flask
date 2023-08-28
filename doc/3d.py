import os

import cv2

script_sdir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(
    script_dir, "/templates/muhammad-asyfaul-gAlbzUkADS4-unsplash.jpg"
)
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_hologram")
def generate_hologram():
    image_path = "/templates/muhammad-asyfaul-gAlbzUkADS4-unsplash.jpg"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    hologram_layers = []
    num_layers = 10  # Number of layers for the hologram effect
    for i in range(num_layers):
        normalized_image = (image / 255.0) * (i / num_layers)
        hologram_layers.append(normalized_image.tolist())  # Convert ndarray to list

    return jsonify({"hologram_layers": hologram_layers})


if __name__ == "__main__":
    app.run(debug=True)
