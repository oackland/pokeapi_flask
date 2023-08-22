from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokemonForm(FlaskForm):
	pokemonName = StringField('Enter Pokémon Name', validators=[DataRequired()])
	submit = SubmitField('Fetch Data')
