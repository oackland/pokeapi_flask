#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    caption = StringField("Caption", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit_btn = SubmitField("Create Post")


class PokemonForm(FlaskForm):
    poke_name = StringField("Pokemon Name", validators=[DataRequired()])
    poke_hp = IntegerField("Pokemon HP", validators=[DataRequired()])
    poke_def = IntegerField("Pokemon Defense", validators=[DataRequired()])
    poke_att = IntegerField("Pokemon Attack", validators=[DataRequired()])
    poke_sprite = StringField("Pokemon Image", validators=[DataRequired()])
    submit_btn = SubmitField("Create Pokemon")
