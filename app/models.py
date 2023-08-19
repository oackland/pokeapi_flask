from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def __repr__(self):
		return f"<User {self.username}>"
