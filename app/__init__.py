from pathlib import Path

from dotenv import load_dotenv
from flask import Flask


def create_app():
    """Create and configure the Flask application."""
    load_dotenv()

    app = Flask(__name__)
    app.config.from_prefixed_env()

    db_path = Path(app.instance_path) / "save.sqlite"
    app.config["DATABASE"] = str(db_path)

    Path(app.instance_path).mkdir(exist_ok=True)

    from app.routes import main

    app.register_blueprint(main)

    return app


def main():  # pragma: no cover
    """CLI entry point."""
    app = create_app()
    app.run()
