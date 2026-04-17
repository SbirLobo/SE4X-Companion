from wtforms import Form
from wtforms.fields import SelectField
from flask_babel import lazy_gettext as _


class PlayerCountForm(Form):
    player_count = SelectField(
        str(_("Number of players")),
        choices=[
            ("", str(_("All"))),
            ("1", str(_("Solo"))),
            ("2", str(_("Duel"))),
            ("3", str(_("3 players"))),
            ("4", str(_("4 players"))),
            ("5", str(_("5 players"))),
            ("6", str(_("6 players"))),
            ("7", str(_("7 players"))),
            ("8", str(_("8 players"))),
            ],
        render_kw= {"onchange": "this.form.submit()"},
        )

class ScenarioTypeForm(Form):
    scenario_type = SelectField(
        str(_("Filter")),
        choices=[
            ("", str(_("All"))),
            ("csb", str(_("Competitive"))),
            ("ssb", str(_("Cooperative"))),
        ],
        render_kw= {"onchange": "this.form.submit()"},
        )
