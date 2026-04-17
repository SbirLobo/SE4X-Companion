from flask import Blueprint
from flask import render_template
from flask import request
from flask_babel import lazy_gettext as _
from app.data.master_rule_book import MASTER_RULEBOOK



rules = Blueprint("rules", __name__)


@rules.route("/rules/view")
def display_rules():
    mrb = MASTER_RULEBOOK
    return render_template("/data/rules.html", mrb=mrb)
