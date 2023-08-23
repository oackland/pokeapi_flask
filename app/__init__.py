# from dotenv import load_dotenv
# from flask import Flask
#
# from config import Config
# from .routes import bp as pokemon_bp
#
# app = Flask(__name__)
# app.config.from_object(Config)
# load_dotenv()
# from . import routes
#
# app.register_blueprint(pokemon_bp)
#
# if __name__ == "__main__":
# 	app.run()
from flask import Flask

from config import Config  # Use relative import here
from .models import db
from .routes import bp as pokemon_bp


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	# Register the blueprint
	app.register_blueprint(pokemon_bp)

	return app


if __name__ == "__main__":
	app = create_app()
	app.run()
