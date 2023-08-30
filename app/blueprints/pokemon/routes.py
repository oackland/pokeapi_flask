#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
# #
# #  The above copyright notice and this permission notice shall be included in all
# #  copies or substantial portions of the Software.
from flask import render_template, request, redirect, url_for

from . import pokemon


#
# @pokemon.route("/pokemon", methods=["GET", "POST"])
# def pokemon():
#     card = Pokemonclass.get_card_by_name("Pikachu")  # Replace "Pikachu" with user input
#     img_url = card.get("images", {}).get(
#         "small"
#     )  # Adjust based on the actual API response
#     return render_template("pokemon.html", img_url=img_url)


@pokemon.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    questions = ["Question 1", "Question 2", "Question 3"]  # Add your questions here
    current_question = int(request.form.get("current_question", 0))

    if request.method == "POST":
        current_question += 1
        if current_question >= len(questions):
            # All questions answered, redirect to a thank-you page or another page
            return redirect(url_for("pokemon.thank_you"))

    return render_template(
        "questionnaire.html", questions=questions, current_question=current_question
    )


@pokemon.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")
