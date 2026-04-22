from flask import Blueprint
from flask import render_template
from flask import request
from flask_babel import lazy_gettext as _
from app.data.master_rule_book import MASTER_RULEBOOK



rules = Blueprint("rules", __name__)


@rules.route("/rules/mrb")
def mrb():
    mrb = MASTER_RULEBOOK
    return render_template("/rules/mrb.html", mrb=mrb)
