from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Optional, Length


class PokemonCardForm(FlaskForm):
    card_name = StringField("Card Name", validators=[DataRequired()])
    abilities = TextAreaField("Abilities (JSON Format)", validators=[Optional()])
    artist = StringField("Artist", validators=[DataRequired(), Length(max=200)])
    ancientTrait = StringField(
        "Ancient Trait", validators=[Optional(), Length(max=200)]
    )
    attacks = TextAreaField("Attacks (JSON Format)", validators=[Optional()])
    weaknesses = TextAreaField("Weaknesses (JSON Format)", validators=[Optional()])
    submit = SubmitField("Submit")


class InitialDataForm(FlaskForm):
    user_idel = StringField("Username", validators=[DataRequired()])
    team = SelectField(
        "Select a team",
        choices=[("team1", "Team 1"), ("team2", "Team 2"), ("team3", "Team 3")],
        validators=[DataRequired()],
    )
    pokemon = SelectField(
        "Select an initial Pokemon",
        choices=[("pokemon1", "Pikachu"), ("pokemon2", "Charmane")],
        validators=[DataRequired()],
    )


class QuestionnaireForm(FlaskForm):
    name = StringField("Name")
    gender = RadioField(
        "Gender", choices=[("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
