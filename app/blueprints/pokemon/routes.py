from flask import render_template

from app.models import InitialData
from app.models import db
from . import pokemon
from .forms import InitialDataForm


@pokemon.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    form = InitialDataForm()

    if form.validate_on_submit():
        new_data = InitialData(
            user_id=1,
            level=1,
            xp=0,
            items={},
            pokemon=form.pokemon.data,
            team=form.team.data,
            user_idel=form.user_idel.data,
            user_idmove="",
        )
        db.session.add(new_data)
        db.session.commit()
        return render_template("thank_you.html")

    return render_template("questionnaire.html", form=form)


@pokemon.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")
