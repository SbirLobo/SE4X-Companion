import re
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask import session
from flask_babel import Babel
from flask import request


_HIGHLIGHT_MAP = [
    ('b', 'blue'),
    ('g', 'green'),
    ('p', 'purple'),
    ('t', 'beige'),
]


def highlight_marks(text):
    """Convert [b]...[/b] shorthand to <mark class="hl-..."> tags."""
    text = str(text)
    for code, color in _HIGHLIGHT_MAP:
        text = re.sub(
            rf'\[{code}\](.*?)\[/{code}\]',
            rf'<mark class="hl-{color}">\1</mark>',
            text,
            flags=re.DOTALL,
        )
    return text


def linkify_sections(text):
    """Replace section references like [4.0], [MRB 4.0] with anchor links."""
    text = str(text)
    pattern = r'\[(MRB|CSB|SSB)? ?(\d+\.\d[\d.]*)\]'

    ob = '<mark class="hl-green">[</mark>'
    cb = '<mark class="hl-green">]</mark>'

    def replace(m):
        prefix, ref = m.group(1), m.group(2)
        anchor = ref.replace('.', '-')
        if prefix == 'MRB':
            return f'<a href="/rules/mrb#{anchor}">{ob}MRB {ref}{cb}</a>'
        if prefix == 'CSB':
            return f'<a href="/rules/csb#{anchor}">{ob}CSB {ref}{cb}</a>'
        if prefix == 'SSB':
            return f'<a href="/rules/ssb#{anchor}">{ob}SSB {ref}{cb}</a>'
        return f'<a href="#{anchor}">{ob}{ref}{cb}</a>'

    return highlight_marks(re.sub(pattern, replace, text))

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
    app.jinja_env.filters['highlight_marks'] = highlight_marks

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
