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
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config  # Use relative import here
from .models import db, User
from .routes import bp as pokemon_bp


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	# db Initialize
	login_manager = LoginManager()
	db.init_app(app)
	migrate = Migrate(app, db)
	login_manager.init_app(app)

	# Register the blueprint
	app.register_blueprint(pokemon_bp)

	@login_manager.user_loader
	def load_user(user_id):
		return User.get(user_id)

	from . import routes, models

	return app


if __name__ == "__main__":
	app = create_app()
	app.run()
