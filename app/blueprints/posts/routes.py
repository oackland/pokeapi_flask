from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user, login_required

from app.models import db, Post
from . import posts
from .forms import PostForm, PokemonForm


# Create a post
@posts.route("/create_post", methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if request.method == "POST" and form.validate_on_submit():
        # Grabbing our post form data
        title = form.title.data
        caption = form.caption.data
        img_url = form.img_url.data
        user_id = current_user.id

        # Creating an instance of the Post Model
        new_post = Post(title, caption, img_url, user_id)

        # Adding new post to our database
        db.session.add(new_post)
        db.session.commit()
        flash(f"Successfully created post {title}!", "primary")

        return redirect(url_for("main.index"))
    else:
        return render_template("create_post.html", form=form)


# Viewing all posts
@posts.route("/feed")
def feed():
    posts = Post.query.all()
    return render_template("feed.html", posts=posts)


# Update a post
@posts.route("/update/<int:post_id>", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm()

    if current_user.id != post.user_id:
        flash("You cannot update someone else's post you snake! 🐍 ", "warning")
        return redirect(url_for("posts.feed"))

    if request.method == "POST" and form.validate_on_submit():
        # form data
        title = form.title.data
        caption = form.caption.data
        img_url = form.img_url.data

        # update post object in db
        post.title = title
        post.caption = caption
        post.img_url = img_url

        # commit changes to db
        db.session.commit()

        return redirect(url_for("posts.feed"))
    else:
        return render_template("update_post.html", post=post, form=form)


# delete post
@posts.route("/delete/<int:post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if current_user.id != post.user_id:
        flash("You cannot delete someone else's post.", "warning")
        return redirect(url_for("posts.feed"))

    db.session.delete(post)
    db.session.commit()

    flash("Post deleted successfully.", "success")
    return redirect(url_for("posts.feed"))


@posts.route("/catch_pokemon", methods=["GET", "POST"])
def catch_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        # Process the form data and create a new Pokemon
        poke_name = form.poke_name.data
        poke_hp = form.poke_hp.data
        poke_def = form.poke_def.data
        poke_att = form.poke_att.data
        poke_sprite = form.poke_sprite.data

        # Perform the necessary actions to create a new Pokemon
        # For example, you can create a new instance of the Pokemon model and save it to the database

        # Redirect to a success page or another route
        return "you got it"

    return render_template("catch_pokemon.html", form=form)
