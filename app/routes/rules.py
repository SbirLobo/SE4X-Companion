from flask import Blueprint
from flask import render_template
from flask import request
from flask_babel import lazy_gettext as _
from app.data.master_rule_book import MASTER_RULEBOOK
from app.data.competitive_scenario_book import CSB_RULES


rules = Blueprint("rules", __name__)


@rules.route("/rules/mrb")
def mrb():
    mrb = MASTER_RULEBOOK
    return render_template("/rules/mrb.html", mrb=mrb)


@rules.route("/rules/csb")
def csb():
    csb = CSB_RULES
    return render_template("/rules/csb.html", csb=csb)
