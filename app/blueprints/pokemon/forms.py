#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import NumberRange


class InitialDataForm(FlaskForm):
    team = StringField("Team")
    user_idel = StringField("User Idel")
    user_idmove = StringField("User Idmove")
    level = IntegerField("Level", validators=[NumberRange(min=1)])
    xp = IntegerField("XP", validators=[NumberRange(min=0)])
    items = TextAreaField("Items")
    pokemon = TextAreaField("Pokemon")
