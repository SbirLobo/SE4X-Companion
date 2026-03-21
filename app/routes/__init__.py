from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask_babel import lazy_gettext as _

from app.db import Game

main = Blueprint("main", __name__)


@main.route("/")
def home():
    print(_("Hello World !"))
    games = Game.query.order_by(Game.updated_at.desc()).all()
    return render_template("home.html", games=games)


@main.route("/set-lang")
def set_lang():
    print(request.args["lang"])
    session["lang"] = request.args["lang"]
    return redirect(request.referrer or url_for("main.home"))
