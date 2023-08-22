from flask import Flask

from config import Config
from .routes import bp as pokemon_bp

app = Flask(__name__)
app.config.from_object(Config)
from . import routes

app.register_blueprint(pokemon_bp)

if __name__ == "__main__":
	app.run()
