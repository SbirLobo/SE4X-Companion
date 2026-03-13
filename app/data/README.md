# Game Data Files

Space Empires 4X — All Good Things
©2024 GMT Games, LLC

## Files

- `card_manifest.json` — All game cards (241 entries)
- `deep_space_planet_attributes.json` — Planet attribute counters (28 entries)
- `game_options.json` — Game options & variants (70 entries)

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
