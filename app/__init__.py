from flask import Flask
from .routes import bp as pokemon_bp
from config import SECRET_KEY, DATABASE_URL

app = Flask(__name__)
app.register_blueprint(pokemon_bp)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
