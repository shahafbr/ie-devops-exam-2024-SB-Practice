from character_api import app
import pytest


    # Exercise III: Develop tests covering ALL THE ROUTES

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    # Implement below:
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404


def test_get_characters(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    # Implement here and below:
    with app.test_client() as client:
        response = client.get('/characters')
        assert response.status_code == 200

from character_api.models import Character
from character_api import db

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (POST)
    THEN check the response is valid and character is created with correct properties
    """
    with app.app_context():
        # Make sure the character does not exist already
        existing = Character.query.get('test_alias')
        if existing:
            db.session.delete(existing)
            db.session.commit()

    with app.test_client() as client:
        response = client.post('/characters', json={
            'alias': 'test_alias',
            'name': 'Test Character',
            'level': 1,
            'health': 100,
            'strength': 10,
            'defense': 5,
            'speed': 7
        })
        assert response.status_code == 200

    with app.app_context():
        character = Character.query.get('test_alias')
        assert character is not None
        assert repr(character) == "Character(Test Character, level=1, health=100.0, strength=10.0, defense=5.0, speed=7.0)"


