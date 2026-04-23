import re
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask import session
from flask_babel import Babel
from flask import request


def linkify_sections(text):
    """Replace section references like (4.0), (MRB 4.0), (CSB 1.1) with anchor links."""
    # erreur : (SSB 3.0 and CSB 10.0)
    # erreur : (RP, 40.5) (3.2, 4.2)
    # faire également les cards #
    # attention aux cards de type #31*
    # et aux cartes -#55
    # et aux cartes #p5
    # passer tous les crochets en vert uo mettre des crochets partout
    text = str(text)
    pattern = r'\((MRB|CSB|SSB)? ?(\d+\.\d[\d.]*)\)'

    def replace(m):
        prefix, ref = m.group(1), m.group(2)
        anchor = ref.replace('.', '-')
        if prefix == 'MRB':
            return f'(MRB <a href="/rules/mrb#{anchor}">{ref}</a>)'
        if prefix == 'CSB':
            return f'(CSB <a href="/rules/csb#{anchor}">{ref}</a>)'
        if prefix == 'SSB':
            return f'(SSB <a href="/rules/ssb#{anchor}">{ref}</a>)'
        return f'(<a href="#{anchor}">{ref}</a>)'

    return re.sub(pattern, replace, text)

def get_locale():
    lang = session.get("lang") if session.get("lang") else request.accept_languages.best_match(["en", "fr"])
    return lang


def create_app():
    """Create and configure the Flask application."""
    load_dotenv()

    app = Flask(__name__)
    app.config.from_prefixed_env()

    app.config.setdefault("BABEL_DEFAULT_LOCALE", "en")
    app.config.setdefault("BABEL_TRANSLATION_DIRECTORIES", "translations")


    babel = Babel(app, locale_selector=get_locale)

    db_path = Path(app.instance_path) / "save.sqlite"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    Path(app.instance_path).mkdir(exist_ok=True)

    from app.db import db
    from app.routes import main
    from app.routes.new_game import new_game
    from app.routes.rules import rules
    from app.routes.cards import cards

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(new_game)
    app.register_blueprint(rules)
    app.register_blueprint(cards)

    app.jinja_env.filters['linkify_sections'] = linkify_sections

    @app.context_processor
    def inject_now():
        return {"now": datetime.now(timezone.utc)}

    @app.context_processor
    def inject_locale():
        from flask_babel import get_locale
        return {"get_locale": get_locale}

    return app


def main():  # pragma: no cover
    """CLI entry point."""
    import os
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3000)))
