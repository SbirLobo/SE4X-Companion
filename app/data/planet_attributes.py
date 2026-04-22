# This file is auto-generated from the JSON source.
# Translatable strings are wrapped with _(). Do not edit manually.
from flask_babel import Domain
_ = Domain(domain='planet_attributes').lazy_gettext

DEEP_SPACE_PLANET_ATTRIBUTES = [
    {
        'number': 1,
        'name': _("""<mark class=\"hl-blue\">Aggressive</mark>"""),
        'ships': 4,
        'heavy_infantry': 0,
        'quantity': 2,
        'PAC_planets_text': [
            _("""Reveal all NPA ships in this hex when the counter is flipped. These ships attack units that end their move in an adjacent hex, then instantly “blink” back to their own planet afterwards without having to take the time to move normally. They will defend against attacks on their own planet first, then will attack a fleet in a random adjacent hex (do not trigger Reaction Movement). They will not attack into a player’s Home System or into <span class="text-uppercase">Thick Asteroids #117</span>, and they will not attack other NPAs. <span class="text-uppercase">Aggressive</span> NPAs are immune to Mines; however, they lose this feature if they are captured or join <span class="text-uppercase">Amazing Diplomats #48 #93</span>. They will attack Deep Space player Colonies, but only after attacking ships in other adjacent hexes. If they defeat the defenses of a Colony, it is automatically destroyed. If all <span class="text-uppercase">Aggressive</span> NPA ships are destroyed while in a hex adjacent to their own planet, randomly draw one NPA ship and place it on their planet. This Attribute is removed when the planet is colonized."""),            ],
        'card_manifest_text': [
            _("""Immediately reveal all NPA ships in this hex when the counter is flipped. These ships attack units that end their move in an adjacent hex, then instantly move back to their own planet afterwards. During any combat phase <span class="text-uppercase">Aggressive</span> NPAs will defend against attacks on their own planet first, then will attack units in adjacent hexes one by one (choose the order randomly if multiple hexes eligible, colony hexes last, see below) until they are destroyed or no enemy units remain in eligible adjacent hexes. These attacks do not trigger Reaction Movement (35.0). <span class="text-uppercase">Aggressive</span> NPAs will never attack units in home systems or <span class="text-uppercase">Thick Asteroids #117</span>. They will also not attack NPAs except ones captured by players (they will attack solo Alien Empire opponent units)."""),
            _("""They will only attack units in hexes with deep space colonies once no units remain in hexes without colonies. If the defending units are destroyed any colony is automatically destroyed too without bombardment. <span class="text-uppercase">Aggressive</span> NPAs do not cause mines to be detonated (this is an exception to 17.1.4); however, they lose this feature if they are captured or join <span class="text-uppercase">Amazing Diplomats #48 #93</span>. If all <span class="text-uppercase">Aggressive</span> NPA ships are destroyed while in a hex adjacent to their own planet, randomly draw one NPA ship and place it on their planet, this ship will not perform any more attacks until the next combat phase. This Attribute is removed when the planet is colonized."""),
            ],
        'errata': '',
    },
    {
        'number': 2,
        'name': _("""<mark class=\"hl-blue\">Spice</mark>"""),
        'ships': 0,
        'heavy_infantry': 4,
        'quantity': 1,
        'PAC_planets_text': [
            _("""This planet can only be taken via Ground Combat; it can never be colonized with a Colony Ship. If an attempt to take this planet fails, the next invasion force will again face 4 Heavy Infantry and 5 Militia. Once conquered by a player, future invasions will only need to defeat that player’s Ground Units (without the replenished Heavy Infantry). If a player’s Colony is destroyed from space, the now empty planet will once again be guarded by 4 HI and 5 Militia. If a full-strength Colony is on the planet at the end of an Economic Phase, all that player’s ships (in supply, 36.5) move at a rate 1 technology level higher until the next Economic Phase. Replicators (40.0) also receive this benefit. If a Replicator Colony is removed from this planet, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""This planet can only be taken via Ground Combat (21.8); it can never be colonized with a Colony Ship. If an attempt to take this planet fails, the next invasion force will again face 4 Heavy Infantry and 5 Militia. Once conquered by a player, future invasions will only need to defeat that player’s Ground Units (without the replenished Heavy Infantry). If a player’s Colony is destroyed by bombardment, the now empty planet will once again be guarded by 4 HI and 5 Militia. If a full-strength Colony is on the planet at the end of an Economic Phase, all that player’s ships (in supply, 36.5) move at a rate 1 technology level higher until the next Economic Phase. Replicators (40.0) also receive this benefit. If a Replicator Colony is removed from this planet, remove this Attribute."""),
            ],
        'errata': '',
    },
    {
        'number': 3,
        'name': _("""<mark class=\"hl-blue\">Organia</mark>"""),
        'ships': 0,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""This planet cannot be conquered, colonized, or connected to a player’s trade network (13.2.2). No combat can occur in this planet’s hex, but it may be moved or retreated into even if enemy ships are present in the hex. Treat this space as a Galactic Capitol (28.1) for purposes of movement restrictions. Because combat is forbidden, Replicators do not gain RPs from other ships in this hex, even for encountering an NPA (18.0)."""),
            ],
        'card_manifest_text': [
            _("""This planet cannot be conquered, colonized, or connected to a player’s trade network (13.2.2). No combat can occur in this planet’s hex, but it may be moved or retreated into even if enemy ships are present in the hex. Treat this space as a Galactic Capitol (28.1) for purposes of movement restrictions. Because combat is forbidden, Replicators do not gain RPs from other ships in this hex, even for encountering an NPA (18.0)."""),
            ],
        'errata': '',
    },
    {
        'number': 4,
        'name': _("""<mark class=\"hl-blue\">Dilithium Crystals</mark>"""),
        'ships': 5,
        'heavy_infantry': 2,
        'quantity': 1,
        'PAC_planets_text': [
            _("""At the end of every Econ Phase during which there is a full-strength Colony on this planet, place a Dilithium counter on the planet if there isn’t one already. A Transport can carry this (and only this) counter to its Homeworld. If successfully transported, the Dilithium counter provides a number of CP equal to the distance from this planet to the Homeworld. Use the shortest possible route when calculating distance, taking into effect Warp Points and Folds in Space but not <span class="text-uppercase">Warp Gates</span>. If Replicators grow a Colony on this planet to full-strength, they remove this Attribute and gain 10 CPs."""),
            ],
        'card_manifest_text': [
            _("""At the end of every Economic Phase during which there is a full-strength Colony on this planet, place a Dilithium counter on the planet if there isn’t one already (if all Dilithium counters are already on the map no additional one is placed). The player who owns this Colony may use a Transport (21.1) to carry one counter (and nothing else) to their Homeworld. If successfully transported, the Dilithium counter provides a number of CP equal to the distance from this planet to the Homeworld. Use the shortest possible route when calculating distance, taking into effect Warp Points (28.2) and Folds in Space (25.2) but not <span class="text-uppercase">Warp Gates</span>. If Replicators grow a Colony on this planet to full-strength, they remove this Attribute and gain 10 CP. If a player’s Colony on this planet is conquered or destroyed (including if a Titan destroys the planet), any existing Dilithium counters carried by that player’s Transports which originated from this planet may still provide CP upon arrival to their Homeworld."""),
            ],
        'errata': '',
    },
    {
        'number': 5,
        'name': _("""<mark class=\"hl-blue\">Abundant</mark>"""),
        'ships': 5,
        'heavy_infantry': 2,
        'quantity': 2,
        'PAC_planets_text': [
            _("""This planet produces 2 extra CPs each Economic Phase during which there is a Colony here, even if the Colony is new. Affects Replicators normally (they treat this as Mineral CP, 40.6.1)."""),
            ],
        'card_manifest_text': [
            _("""This planet produces 2 extra CP each Economic Phase during which there is a Colony here, even if the Colony is new. Replicators treat this as Mineral CP (40.6.1)"""),
            ],
        'errata': '',
    },
    {
        'number': 6,
        'name': _("""<mark class=\"hl-blue\">Wealthy</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 2,
        'PAC_planets_text': [
            _("""This planet produces 1 extra CP each Economic Phase during which there is a Colony here, even if the Colony is new. If a Replicator Colony is placed here, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""This planet produces 1 extra CP each Economic Phase during which there is a Colony here, even if the Colony is new. If a Replicator Colony is placed here, remove this Attribute <i>(the wealth comes from the native economy; Replicators would ignore it)</i>."""),
            ],
        'errata': '',
    },
    {
        'number': 7,
        'name': _("""<mark class=\"hl-blue\">Poor</mark>"""),
        'ships': 2,
        'heavy_infantry': 0,
        'quantity': 2,
        'PAC_planets_text': [
            _("""This planet produces 1 less CP each Economic Phase during which there is a Colony here, to a minimum of 0. If a Replicator Colony is placed here, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""This planet produces 1 less CP each Economic Phase during which there is a Colony here, to a minimum of 0. If a Replicator Colony is placed here, remove this Attribute (the lack of wealth comes from the native economy; Replicators would ignore it)."""),
            ],
        'errata': '',
    },
    {
        'number': 8,
        'name': _("""<mark class=\"hl-blue\">Desolate</mark>"""),
        'ships': 1,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""This planet produces 4 less CP each Economic Phase during which there is a Colony here, to a minimum of 0. Replicators must pay 3 CP during an Economic Phase to produce a ship at this planet, but a Replicator Colony at full strength may always be used to join/split/reconfigure Replicator ships without cost."""),
            ],
        'card_manifest_text': [
            _("""This planet produces 4 less CP each Economic Phase during which there is a Colony here, to a minimum of 0. Replicators do not produce a ship at this planet during an Economic Phase unless the Colony is at Full and they pay 3 CP, but a Replicator Colony at full strength may always be used to join/split/reconfigure Replicator ships without cost (40.3.2)."""),
            ],
        'errata': '',
    },
    {
        'number': 9,
        'name': _("""<mark class=\"hl-blue\">Sparta</mark>"""),
        'ships': 0,
        'heavy_infantry': 3,
        'quantity': 1,
        'PAC_planets_text': [
            _("""At the end of any Econ Phase, if there is a full-strength Colony on this planet, that Colony produces either one Space Marine or one Heavy Infantry (if the Colony’s owner has Ground Combat 2.) If a Replicator Colony is placed on this planet, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""At the end of any Economic Phase during which there is a full-strength Colony on this planet, that Colony additionally produces either one Space Marine or one Heavy Infantry (if the Colony’s owner does not have Ground Combat 2 no unit is produced) If a Replicator Colony is placed on this planet, remove this Attribute."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text corrected per PAC Planets: 'does not have' — Card Manifest reads 'has Ground Combat 2 no unit is produced' (inverted condition, likely a typo in the Card Manifest).</mark>"""),
    },
    {
        'number': 10,
        'name': _("""<mark class=\"hl-blue\">Defensible</mark>"""),
        'ships': 4,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All defending Ground Units (including Militia) on this planet get +1 Defense Strength. There is no extra effect on colony bombardment rolls."""),
            ],
        'card_manifest_text': [
            _("""All defending Ground Units (including Militia) on this planet get +1 Defense Strength. There is no extra effect on colony bombardment rolls."""),
            ],
        'errata': '',
    },
    {
        'number': 11,
        'name': _("""<mark class=\"hl-blue\">Dampening</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All ships must stop before and after entering this planet hex. All ships must also stop after leaving this hex. Nothing can remove this movement restriction, including MS Pipelines (13.2.1). However, an MS Pipeline can still connect to the Colony and provide its standard increase to CP."""),
            ],
        'card_manifest_text': [
            _("""Because of a strong dampening field that interferes with FTL travel, all ships must stop after entering this planet hex. All ships must also stop after leaving this hex. Nothing can remove this movement restriction, including MS Pipelines (13.2.1). However, an MS Pipeline can still connect to the Colony and provide its standard increase to CP."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text corrected per PAC Planets: added 'before and' to movement restriction.</mark>"""),
    },
    {
        'number': 12,
        'name': _("""<mark class=\"hl-blue\">Ambush</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All attacking ships (including <span class="text-uppercase">Longbowmen #59</span> ships) in this hex fire as if they are E-Class. Boarding Ships still fire as F-Class. If a Replicator Colony is placed on this planet, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""All attacking ships in this hex fire as if they are E-Class (this supersedes any effects from cards). Boarding Ships still fire as F-Class. If a Replicator Colony is placed on this planet, remove this Attribute."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text corrected per PAC Planets: added '(including <span class="text-uppercase">Longbowmen #59</span> ships)'. Note: PAC Planets omits '(this supersedes any effects from cards)' — Card Manifest includes it; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 13,
        'name': _("""<mark class=\"hl-blue\">Doomed</mark>"""),
        'ships': 1,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""When this planet is revealed, place a numeral marker with a 6 in the hex. Reduce the numerical marker by 1 each Economic Phase. When the numeral marker should be reduced from 1 to 0, remove it instead. The planet explodes and destroys all units in the hex; replace it with an Asteroid terrain tile."""),
            ],
        'card_manifest_text': [
            _("""When this planet is revealed, place a numeral marker with a 6 in the hex. Reduce the numerical marker by 1 each Economic Phase. When the numeral marker should be reduced from 1 to 0, remove it instead. The planet explodes and destroys all units in the hex; replace it with an Asteroid counter (or terrain tile.) If this planet is removed for any other reason (Titan attack, Replicator Colony depletion), remove this Attribute and the numerical countdown marker."""),
            ],
        'errata': '',
    },
    {
        'number': 14,
        'name': _("""<mark class=\"hl-blue\">Builder</mark>"""),
        'ships': 5,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""When colonized, this planet provides 3 Hull Points of Shipyard build capacity. These Hull Points are available as long as there is a Colony on the planet, but they are not impacted by technology. If a Replicator Colony is placed on this planet, remove this Attribute."""),
            ],
        'card_manifest_text': [
            _("""Any colony on the planet is treated as having a shipyard capacity of 3 in addition to any shipyard in the hex. This is not modified by technology and provides no benefit in combat. Ships can be retrofitted in this hex as if an SY was present. If a Replicator Colony is placed on
this planet, remove this Attribute."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text replaced per PAC Planets: '3 Hull Points of Shipyard build capacity'.</mark>"""),
    },
    {
        'number': 15,
        'name': _("""<mark class=\"hl-blue\">Spaceport</mark>"""),
        'ships': 0,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""This planet is a neutral spaceport and cannot be colonized or fired upon, though it can be connected to a player’s trade network as if it were a Colony. It may not have Fighters or Ground Units on the planet. Combat occurs normally in the hex, but the planet is always unaffected. A player who has a unit in this hex at the start of the Economic Phase may build one ship of Ship Size 1 in this hex for 2 CP more than that ship’s usual cost. A Raider using Cloak to avoid combat does not allow a player the ability to build a ship here. A Replicator player may place one of their Hulls at this planet instead of at the planet where it would have usually been produced. That Hull will cost 1 CP additional."""),
            ],
        'card_manifest_text': [
            _("""This planet is a neutral spaceport and cannot be colonized or fired upon, though it can be connected to a player’s trade network as if it were a Colony. It may not have Fighters or Ground Units on the planet. Combat occurs normally in the hex, but the planet is always unaffected. A player who has a unit in this hex at the start of the Economic Phase may build one ship of Ship Size 1 in this hex for 2 CP more than that ship’s usual cost. A Raider using Cloak to avoid combat does not allow a player the ability to build a ship here. A Replicator player with units in this hex may move a newly-built Size 1 ship to this hex for 1 CP at the end of the Economic Phase."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text corrected per PAC Planets: Replicator rule reworded to match source.</mark>"""),
    },
    {
        'number': 16,
        'name': _("""<mark class=\"hl-blue\">Research</mark>"""),
        'ships': 5,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""When colonized for the first time (only), this planet gives one level of technology. Roll on the Space Wreck table. If a Replicator Colony is placed on this planet, remove this Attribute and treat the Replicators as if they consumed a Space Wreck, gaining 1 RP."""),
            ],
        'card_manifest_text': [
            _("""When colonized for the first time (only), this planet gives one level of technology. Roll on the Space Wreck table. If a Replicator Colony is placed on this planet, remove this Attribute and treat the Replicators as if they consumed a Space Wreck, gaining 1 RP."""),
            ],
        'errata': '',
    },
    {
        'number': 17,
        'name': _("""<mark class=\"hl-blue\">Minor Technology</mark>"""),
        'ships': 4,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""Instead of drawing two Alien Tech Cards and choosing one, the player draws three and chooses one. Replicators draw one card and discard it, gaining 10 CP as normal."""),
            ],
        'card_manifest_text': [
            _("""Instead of drawing two Alien Technology Cards and choosing one (11.0), the player draws three and chooses one. Replicators gain no additional benefit; they draw one card and immediately discard it, gaining 10 CP as normal."""),
            ],
        'errata': '',
    },
    {
        'number': 18,
        'name': _("""<mark class=\"hl-blue\">Major Technology</mark>"""),
        'ships': 5,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""Instead of drawing two Alien Technology Cards and choosing one, the player draws three and chooses two. Replicators draw only two cards and immediately discard both, gaining 20 CP as normal (10 per card)."""),
            ],
        'card_manifest_text': [
            _("""Instead of drawing two Alien Technology Cards and choosing one (11.0), the player draws three and chooses two. Replicators draw two cards and immediately discard both, gaining 20 CP (10 CP per card as normal)."""),
            ],
        'errata': '',
    },
    {
        'number': 19,
        'name': _("""<mark class=\"hl-blue\">Cloaked</mark>"""),
        'ships': 4,
        'heavy_infantry': 0,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships in this hex have Cloaking 2 but will not cloak to avoid combat. Replicators entering combat with these NPAs are treated as encountering Cloaking, unlocking Scanners."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships in this planet hex have Cloaking 2 but will not cloak to avoid combat. Replicators entering combat with these NPAs are treated as encountering Cloaking, thereby unlocking Scanners."""),
            ],
        'errata': '',
    },
    {
        'number': 20,
        'name': _("""<mark class=\"hl-blue\">Ranged</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here fire as if they are one Weapon Class better. When this planet is first colonized, the player gets 10 CP off the next level of Tactics Technology they research (take the planet counter as a reminder). Replicators entering combat with these NPAs are treated as encountering Tactics 2. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here fire as if they are one Weapon Class better. When this planet is first colonized, the player gets 10 CP off the next level of Tactics Technology they research (the counter is removed and kept as a reminder). Replicators entering combat with these NPAs are treated as encountering Tactics 2, potentially gaining an RP. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'errata': _("""<mark class=\"hl-green\">PAC Planets reads 'take the planet counter as a reminder' — Card Manifest reads 'the counter is removed and kept as a reminder'; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 21,
        'name': _("""<mark class=\"hl-blue\">Accurate</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here have +1 to their Attack Strength. When this planet is first colonized, the player gets 10 CP off the next Attack Technology they research (take the planet counter as a reminder). Replicators entering combat with these NPAs are treated as encountering Attack 1. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here have +1 to their Attack Strength. When this planet is first colonized, the player gets 10 CP off the next Attack Technology they research (the counter is removed and kept as a reminder). Replicators entering combat with these NPAs are treated as encountering Attack 1, potentially gaining an RP. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'errata': _("""<mark class=\"hl-green\">PAC Planets reads 'take the planet counter as a reminder' — Card Manifest reads 'the counter is removed and kept as a reminder'; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 22,
        'name': _("""<mark class=\"hl-blue\">Shielded</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here have +1 to their Defense Strength. When this planet is first colonized, the player gets 10 CP off the next Defense Technology they research (take the planet counter as a reminder). Replicators entering combat with these NPAs are treated as encountering Defense 1. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here have +1 to their Defense Strength. When this planet is first colonized, the player gets 10 CP off the next Defense Technology they research (the counter is removed and kept as a reminder). Replicators entering combat with these NPAs are treated as encountering Defense 1, potentially gaining an RP. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'errata': _("""<mark class=\"hl-green\">PAC Planets reads 'take the planet counter as a reminder' — Card Manifest reads 'the counter is removed and kept as a reminder'; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 23,
        'name': _("""<mark class=\"hl-blue\">Giant</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here have +1 Hull Points. When this planet is first colonized, the player gets 10 CP off the next Ship Size Technology they research (take the planet counter as a reminder). Replicators entering combat with these NPAs are treated as encountering a Cruiser. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here have +1 Hull Points except for determining if they are equipped with Scanner or Point Defense technology. When this planet is first colonized, the player gets 10 CP off the next Ship Size Technology they research (the counter is removed and kept as a reminder). Replicators entering combat with these NPAs are treated as encountering a Cruiser, potentially gaining an RP. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'errata': _("""<mark class=\"hl-green\">PAC Planets reads 'take the planet counter as a reminder' — Card Manifest reads 'the counter is removed and kept as a reminder'; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 24,
        'name': _("""<mark class=\"hl-blue\">Military Geniuses</mark>"""),
        'ships': 4,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here have +1 Attack and +1 Defense. When this planet is colonized, the player draws two Crew Cards (12.0) and keeps one."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here have +1 Attack and +1 Defense. When this planet is colonized, the player draws two Crew Cards (12.0) and keeps one, which can be used immediately or at the next Econ Phase. In addition, whenever a Crew Card is used, it may be placed on a ship in this hex, if colonized."""),
            ],
        'errata': _("""<mark class=\"hl-green\">Text follows Card Manifest (full version). PAC Planets reads 'When this planet is colonized, the player draws two Crew Cards (12.0) and keeps one.' (shorter, without the usage rule). Previous version incorrectly used 'has a Colony' instead of 'is colonized' (wrong per both sources).</mark>"""),
    },
    {
        'number': 25,
        'name': _("""<mark class=\"hl-blue\">Jedun</mark>"""),
        'ships': 5,
        'heavy_infantry': 2,
        'quantity': 1,
        'PAC_planets_text': [
            _("""All NPA ships here have +1 Attack, +1 Defense, and +1 Tactics. When this planet has a Colony, the player may place one group (ships or Ground Units) with up to 8 Hull Points under this Jedun counter; the group is studying at the Jedun Temple. Only one group may be studying at the Jedun Temple at a time and that group may not simultaneously upgrade their ships. If it does not move for three consecutive turns, the group is marked with a Jedun counter for the rest of the game. This group gets +1 Attack, +1 Defense, +1 Tactics to its base stats. These bonuses are not considered technological, but from training at the Jedun temple. It is possible for a group to have an effective rating of Tactics 4 because of this. No units may be added to this group unless they also have a Jedun counter. Jedun ships that are captured are no longer Jedun. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""All NPA ships here have +1 Attack, +1 Defense, and +1 Tactics. When this planet has a Colony, the owner may place one group (ships or Ground Units) with up to 8 Hull Points under this counter; the group is studying at the Jedun Temple. Only one group may be studying at the Jedun Temple at a time and that group may not simultaneously upgrade their ships. If it does not move for three consecutive turns, the group is marked with a Jedun counter for the rest of the game. This group gets +1 Attack, +1 Defense, +1 Tactics to its base stats. These bonuses are not considered technological, but rather a consequence of the disciplined training the crew received at the temple. It is possible for a group to have an effective rating of Tactics 4 because of this. No units may be added to this group unless they also have a Jedun counter and any Group split off gains a Jedun counter. Jedun ships that are captured are no longer Jedun (due to the change in crew). If a Replicator Colony is placed on this planet or the planet is destroyed, remove this Attribute without further effect; preexisting groups with Jedun counters retain their bonuses."""),
            ],
        'errata': _("""<mark class=\"hl-green\">PAC Planets reads 'but from training at the Jedun temple' — Card Manifest reads 'but rather a consequence of the disciplined training the crew received at the temple'; text follows Card Manifest.</mark>"""),
    },
    {
        'number': 26,
        'name': _("""<mark class=\"hl-blue\">Telepathic</mark>"""),
        'ships': 5,
        'heavy_infantry': 1,
        'quantity': 1,
        'PAC_planets_text': [
            _("""If a player has a Colony on this planet, ships that start in the hex and do not move may be placed under the Telepathic counter. At the end of another player's move (before ships are revealed in combat), ships under the Telepathic counter may be placed in any battle hex within range of what they could have moved to in their previous turn. They are considered part of the defending forces from the start of the battle. They may also be placed in a hex adjacent to the Colony with no enemy combat units present. They may do this even if their hex has an attacking fleet in it. This represents the people of the planet warning them of where enemy units are going to move and thereby being able to intercept or avoid them. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'card_manifest_text': [
            _("""If a player has a Colony on this planet, their ships that start in the hex and do not move may be placed under the Telepathic counter. At the end of another player’s movement phase (before ships are revealed in combat), ships under the Telepathic counter may be placed in any battle hex within range of what they could have moved to in their previous turn. They are considered part of the defending forces from the start of the battle. They may also be placed in a hex adjacent to the Colony with no enemy combat units present. They may do this even if their hex has an attacking fleet in it. This represents the people of the planet warning them of where enemy units are going to move and thereby being able to intercept or avoid them. If a Replicator Colony is placed on this planet, remove this Attribute without further effect."""),
            ],
        'errata': '',
    },
    {
        'number': 27,
        'name': _("""<mark class=\"hl-blue\">Scanning</mark>"""),
        'ships': 6,
        'heavy_infantry': 2,
        'quantity': 1,
        'PAC_planets_text': [
            _("""There is a massive scanning array built into this planet which is far beyond the tech of the players. If a player has a Colony on this planet, all enemy ships within 2 hexes of the planet are flipped to their revealed side. If a Replicator Colony is on the planet, they receive the same benefit."""),
            ],
        'card_manifest_text': [
            _("""There is a massive scanning array built into this planet which is far beyond the technology of the players. If a player has a Colony on this planet, all enemy ships within 2 hexes of the planet are flipped to their revealed side (immediately when the colony is placed and immediately when ships enter later). If a Replicator Colony is on the planet, they receive the same benefit."""),
            ],
        'errata': '',
    },
    {
        'number': 28,
        'name': _("""<mark class=\"hl-blue\">Time Dilation</mark>"""),
        'ships': 6,
        'heavy_infantry': 2,
        'quantity': 1,
        'PAC_planets_text': [
            _("""Time moves twice as fast on this planet. During the Economic Phase, a Colony on this planet grows twice and produces twice. A Colony with a 1 marker on it would produce 1 CP, grow to a 3 marker, produce 3 CP, and then grow to a 5 marker in one Economic Phase. Twice as many Shipyards or Bases can be produced in one Economic Phase and each Shipyard can produce twice as many ships. The first Shipyard built on this planet during any one Economic Phase may produce a normal number of ships in that Economic Phase. After combat, the planet may be bombarded by each ship twice. Replicator Colonies are not affected as described above. Replicator Colonies that begin an Economic Phase at full growth may build a single Hull Size 2 ship directly instead of creating two Hull Size 1 ships."""),
            ],
        'card_manifest_text': [
            _("""Time moves twice as fast on this planet. During the Economic Phase, a Colony on this planet grows twice and produces twice. A Colony with a 1 marker on it would produce 1 CP, grow to a 3 marker, produce 3 CP, and then grow to a 5 marker in one Economic Phase. Twice as many Shipyards or Bases can be produced in one Economic Phase as is normally allowed and each existing Shipyard can produce twice as many ships. The first (or only) Shipyard built on this planet during any one Economic Phase may produce a normal number of ships in that Economic Phase. After combat, the planet may be bombarded by each ship twice. Replicator Colonies are not affected as described above. Replicator Colonies that begin an Economic Phase at full growth may build a single Hull Size 2 ship directly instead of creating two Hull Size 1 ships."""),
            ],
        'errata': '',
    },
]
