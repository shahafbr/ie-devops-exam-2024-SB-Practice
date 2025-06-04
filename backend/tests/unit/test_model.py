from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise III: Develop this test according to the definition and make it pass in the GitHub workflow
    character = Character('John Doe','John Doe')
    assert character.alias == 'John Doe'
    assert character.name == 'John Doe'
