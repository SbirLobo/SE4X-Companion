from flask import Blueprint, render_template

from app.db import Game

main = Blueprint("main", __name__)


@main.route("/")
def home():
    games = Game.query.order_by(Game.updated_at.desc()).all()
    return render_template("home.html", games=games)
