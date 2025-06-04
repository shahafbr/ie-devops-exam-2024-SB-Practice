from character_api import app
import pytest

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    # Exercise III: Develop this test according to the definition and make it pass in the GitHub workflow
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_get_characters(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    # Exercise III: Develop this test according to the definition and make it pass in the GitHub workflow
    response = testing_client.get('/characters')
    assert response.status_code == 200

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    # Exercise III: Develop this test according to the definition and make it pass in the GitHub workflow
    response = testing_client.post('/characters', json={'alias': 'John Doe', 'name': 'John Doe'})
    assert response.status_code == 200
