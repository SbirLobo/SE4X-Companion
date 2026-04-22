from flask import Blueprint
from flask import render_template
from flask import request
from flask_babel import lazy_gettext as _

from app.data.cards import CARD_MANIFEST
from app.data.planet_attributes import DEEP_SPACE_PLANET_ATTRIBUTES


cards = Blueprint("cards", __name__)

card_manifest = CARD_MANIFEST
deep_space_planets = DEEP_SPACE_PLANET_ATTRIBUTES

card_types = [
    "alien_technology",
    "empire_advantage",
    "replicator_empire_advantage",
    "resource",
    "scenario_modifier",
    "replicator_crew",
    "crew",
]

@cards.route("/cards")
def cards_index():
    alien_technology_cards = [card for card in card_manifest if card["type"]=="alien_technology"]
    empire_advantage_card = [card for card in card_manifest if card["type"]=="empire_advantage"]
    replicator_empire_advantage_cards = [card for card in card_manifest if card["type"]=="replicator_empire_advantage"]
    resource_cards = [card for card in card_manifest if card["type"]=="resource"]
    scenario_modifier_cards = [card for card in card_manifest if card["type"]=="scenario_modifier"]
    replicator_crew_cards = [card for card in card_manifest if card["type"]=="replicator_crew"]
    crew_cards = [card for card in card_manifest if card["type"]=="crew"]

    sorted_cards = empire_advantage_card + replicator_empire_advantage_cards + alien_technology_cards + crew_cards + replicator_crew_cards + deep_space_planets + scenario_modifier_cards + resource_cards

    return render_template(
    "/cards/index.html",
    sorted_cards=sorted_cards
    )

@cards.route("/planets")
def pac_planets():
    return render_template(
    "/pac/planets.html",
    deep_space_planets=deep_space_planets
    )
