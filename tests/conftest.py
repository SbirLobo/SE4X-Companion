import pytest

from app import create_app
from app.db import db as _db


@pytest.fixture
def app():
    """Create app with testing config and in-memory database."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()
        _db.engine.dispose()


@pytest.fixture
def client(app):
    """HTTP test client."""
    return app.test_client()
