#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)


# Implement the UserMixin methods


def get_id(self):
    return str(self.id)  # Convert to string to satisfy the UserMixin requirement


@property
def is_active(self):
    return True


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    caption = db.Column(db.String)
    img_url = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, title, caption, img_url, user_id):
        self.title = title
        self.caption = caption
        self.img_url = img_url
        self.user_id = user_id


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    description = db.Column(db.Text)

    def __init__(self, user_id, name, me_type, description):
        self.user_id = user_id
        self.name = name
        self.type = me_type
        self.description = description


class PokemonCard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    abilities = db.Column(db.JSON)
    artist = db.Column(db.String())
    ancientTrait = db.Column(db.String())
    attacks = db.Column(db.JSON)
    weaknesses = db.Column(db.JSON)

    def __init__(self, user_id, abilities, artist, ancientTrait, attacks, weaknesses):
        self.user_id = user_id
        self.abilities = abilities
        self.artist = artist
        self.ancientTrait = ancientTrait
        self.attacks = attacks
        self.weaknesses = weaknesses
