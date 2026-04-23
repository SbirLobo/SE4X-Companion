
from flask import Blueprint
from flask import render_template
from flask import request
from flask_babel import lazy_gettext as _
from app.forms import PlayerCountForm
from app.forms import ScenarioTypeForm

from app.db import Game
from app.data.scenario_list import SCENARIO_LIST


new_game = Blueprint("new-game", __name__)


@new_game.route("/new-game/scenario")
def scenario():
    scenarios = SCENARIO_LIST
    player_count_form = PlayerCountForm(request.args)
    scenario_type_form = ScenarioTypeForm(request.args)

    if player_count_form.player_count.data:
        player_count = int(player_count_form.player_count.data)
        scenarios = [scenario for scenario in scenarios if player_count >= scenario["players_min"] and player_count <= scenario["players_max"]]
        scenario_type_form.scenario_type.data = "All" if player_count == 1 else scenario_type_form.scenario_type.data

    if scenario_type_form.scenario_type.data:
        scenario_type = scenario_type_form.scenario_type.data
        scenarios = scenarios if scenario_type == "All" else [scenario for scenario in scenarios if scenario["source"] == scenario_type]


    return render_template(
        "/new_game/scenario.html",
        scenarios=scenarios,
        player_count_form=player_count_form,
        scenario_type_form=scenario_type_form,
        )
