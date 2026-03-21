from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask import session
from flask_babel import Babel
from flask import request

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

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

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
    app = create_app()
    app.run()
