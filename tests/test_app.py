from flask import Flask

from app import create_app


def test_create_app_returns_flask_instance(app):
    assert isinstance(app, Flask)


def test_create_app_sets_database_uri(app):
    assert "SQLALCHEMY_DATABASE_URI" in app.config


def test_create_app_sets_testing_mode(app):
    assert app.config["TESTING"] is True


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_app_name(client):
    response = client.get("/")
    assert b"SE4X Companion" in response.data
    assert b"New Game" in response.data


def test_home_shows_no_games_message(client):
    response = client.get("/")
    assert b"No saved games yet" in response.data
