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

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (POST)
    THEN check the response is valid
    """
    # Implement here and below:
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

def test_character_level_up(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters/<alias>/level_up' page is requested (POST)
    THEN check the response is valid
    """
    # Implement here and below:
    with app.test_client() as client:
        response = client.post('/characters/test_alias/level_up')
        assert response.status_code == 200