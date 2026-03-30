TRANSLATIONS = app/translations
LANGS = fr
DATA_DOMAINS = cards game_elements game_options master_rulebook planet_attributes scenario_rulebooks scenarios_list tables

.PHONY: babel-extract babel-update babel-compile babel-all

babel-extract:
	pybabel extract -F pyproject.toml -o $(TRANSLATIONS)/messages.pot .
	$(foreach d,$(DATA_DOMAINS),pybabel extract app/data/$(d).py -o $(TRANSLATIONS)/$(d).pot;)

babel-update:
	pybabel update -i $(TRANSLATIONS)/messages.pot -d $(TRANSLATIONS) -D messages
	$(foreach d,$(DATA_DOMAINS),pybabel update -i $(TRANSLATIONS)/$(d).pot -d $(TRANSLATIONS) -D $(d);)

babel-compile:
	pybabel compile -d $(TRANSLATIONS) -D messages
	$(foreach d,$(DATA_DOMAINS),pybabel compile -d $(TRANSLATIONS) -D $(d);)

babel-all: babel-extract babel-update babel-compile
