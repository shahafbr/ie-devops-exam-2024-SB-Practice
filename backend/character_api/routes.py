from flask import Flask, request
from character_api import db, app
from character_api.models import Character

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    alias = data['alias']
    name = data['name']
    level = data.get('level', 1)
    health = data.get('health', 100.0)
    strength = data.get('strength', 5.0)
    defense = data.get('defense', 5.0)
    speed = data.get('speed', 5.0)

    if not Character.query.get(alias):
        character = Character(alias, name)
        character.level = level
        character.health = health
        character.strength = strength
        character.defense = defense
        character.speed = speed

        db.session.add(character)
        db.session.commit()
        return format_character(character)
    else:
        return "Character already exists", 400

def format_character(character):
    return {
        "alias": character.alias,
        "name": character.name,
        "level": character.level,
        "health": character.health,
        "strength": character.strength,
        "defense": character.defense,
        "speed": character.speed
    }
