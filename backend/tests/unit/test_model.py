from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise III: Develop this test according to the definition and make it pass in the GitHub workflow
    character = Character(alias="hero", name="Hero", level=1, health=100, strength=10, defense=5, speed=7)
    assert character.alias == "hero"
    assert character.name == "Hero"
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 10
    assert character.defense == 5
    assert character.speed == 7


    # Exercise III: Add at least one more unit test
def test_character_level_up():
    """
    GIVEN a Character model
    WHEN the level_up method is called
    THEN check the level increases by 1
    """ 
    character = Character(alias="hero", name="Hero", level=1, health=100, strength=10, defense=5, speed=7)
    initial_level = character.level
    character.level_up()
    assert character.level == initial_level + 1

