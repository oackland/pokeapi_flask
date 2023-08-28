from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config
from .models import User, db


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	# db Initialize
	login_manager = LoginManager()
	db.init_app(app)
	migrate = Migrate(app, db)
	login_manager.init_app(app)

	login_manager.login_view = 'login'
	login_manager.login_message = 'danger'
	# Register the blueprint

	from app.blueprints.auth import auth
	from app.blueprints.main import main
	from app.blueprints.posts import posts

	app.blueprints = [auth, main, posts]

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(user_id)

	from . import models

	return app


if __name__ == "__main__":
	app = create_app()
	app.run()
