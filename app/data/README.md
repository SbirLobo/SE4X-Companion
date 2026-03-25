# Game Data Files

Space Empires 4X — All Good Things
©2024 GMT Games, LLC

## Files

- `master_rulebook.json` — Complete AGT Master Rule Book text (442 entries)
- `scenarios.json` — All scenarios from both AGT scenario books (68 entries)
- `scenario_rules.json` — Shared rules, forewords, gameplay advice (11 entries)
- `game_elements.json` — Ships, technologies, exploration results, ground units
- `game_options.json` — Game options & variants (74 entries)
- `card_manifest.json` — All game cards (241 entries)
- `deep_space_planet_attributes.json` — Planet attribute counters (28 entries)
- `tables.json` — Structured game tables: difficulty, strength, technology, combat (34 tables)

### Table references

Other JSON files may reference a table with `[TABLE:id]` instead of embedding the table data inline.
Example: `"[TABLE:dm_strength]"` in `master_rulebook.json` refers to the `dm_strength` entry in `tables.json`.

## Source documents

| Abbrev.        | Document                                                      |
|----------------|---------------------------------------------------------------|
| MRB            | All Good Things - Master Rule Book (v1.0)                     |
| CSB            | All Good Things - Competitive Scenario Book (v1.0)            |
| SSB            | All Good Things - Solo/Co-op Scenario Book (v1.0)             |
| Card Manifest  | All Good Things - Card Manifest (v5)                          |
| PAC Planets    | All Good Things - Player Aid Card #1 — Planets (v3)           |
|                | All Good Things - Production Sheet No Facilities (v3)         |
|                | All Good Things - Production Sheet Facilities (v2)            |
|                | All Good Things - Replicator Production Sheet (v3)            |
|                | All Good Things - Player Aid Card Base Empire (v1)            |
|                | All Good Things - Player Aid Card Alternate Empire (v1)       |
|                | Base game Rule Book                                           |
|                | Base game Scenario Book                                       |
|                | Close Encounters Rule Book                                    |
|                | Close Encounters Scenario Book                                |
|                | Replicators Rule Book                                         |

## highlighted fields

### card_manifest.json — `highlighted`

Editorial note indicating that the card text was corrected or clarified relative to the original printed card. The correction source is always a GMT Games player aid card (e.g. *PAC Planets v3*).

Example: `"Text corrected per PAC Planets: added '(including LONGBOWMEN ships)'."`

### deep_space_planet_attributes.json — `highlighted`

Same purpose: flags that the planet attribute text differs from the printed counter and was corrected via a GMT Games player aid card.

Example: `"Text corrected per PAC Planets: added 'before and' to movement restriction."`

### master_rulebook.py / scenarios.py / scenario_rules.py — inline highlight fields

The AGT source documents (MRB, SSB, CSB) use three types of visual highlighting with explicit meaning defined on page 2 of each book. Relevant entries carry one or more of the following fields (lists of translatable strings):

| Field | Highlight color | Meaning |
|-------|----------------|---------|
| `highlighted_updated_notes` | Light blue | New or updated Space Empires rules |
| `highlighted_play_notes` | Purple | Play Notes (clarifications on how rules work in practice) |
| `highlighted_design_notes` | Tan/beige | Design Notes (designer commentary) |

Only entries that have at least one highlighted passage carry these fields. Absent field = no highlight of that type in the source document for that section.

---

## game_options.json fields

| Field          | Description                                                     |
|----------------|-----------------------------------------------------------------|
| `id`           | Unique identifier (slug)                                        |
| `name`         | Official rule name                                              |
| `ref`          | Where to find this rule — list of `"Book Name, section, p.XX"` |
| `category`     | Rule grouping (see below)                                       |
| `default`      | Whether this option is typically used (author recommendation)   |
| `source`       | Expansion that introduced this option (see below)               |
| `requires`     | List of option ids that must be enabled first                   |
| `incompatible` | List of option ids that cannot be used together                 |
| `description`  | Rule summary                                                    |

### Categories

| Value                  | Description                                                |
|------------------------|------------------------------------------------------------|
| `extension`            | Rules adding new components (cards, units)                 |
| `advanced`             | Major gameplay modules                                     |
| `optional`             | Rules changing game pace or flavor                         |
| `additional_terrain`   | Sub-options of Additional Terrain (25.0)                   |
| `advanced_construction`| Sub-options of Advanced Construction (38.0)                |
| `facility`             | Sub-options of Facilities (36.0)                           |
| `variant`              | Lightweight gameplay tweaks                                |
| `deprecated`           | Old variants absent from AGT documents (kept for reference)|

### Sources

| Value  | Expansion                        |
|--------|----------------------------------|
| `base` | Base game                        |
| `ce`   | Close Encounters                 |
| `r`    | Replicators                      |
| `agt`  | All Good Things                  |
