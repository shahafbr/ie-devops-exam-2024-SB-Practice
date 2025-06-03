from flask import request
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

    if db.session.get(Character, alias):
        return {"error": "Character already exists"}, 400

    character = Character(alias, name, level, health, strength, defense, speed)
    db.session.add(character)
    db.session.commit()
    return format_character(character), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return {'characters': [format_character(character) for character in characters]}, 200

@app.route('/characters/<string:alias>', methods=['GET'])
def get_character(alias):
    character = db.session.get(Character, alias)
    if not character:
        return {"error": "Character not found"}, 404
    return format_character(character), 200

@app.route('/characters/<string:alias>', methods=['PUT'])
def update_character(alias):
    character = db.session.get(Character, alias)
    if not character:
        return {"error": "Character not found"}, 404

    data = request.json
    character.name = data.get('name', character.name)
    character.level = data.get('level', character.level)
    character.health = data.get('health', character.health)
    character.strength = data.get('strength', character.strength)
    character.defense = data.get('defense', character.defense)
    character.speed = data.get('speed', character.speed)

    db.session.commit()
    return format_character(character), 200

@app.route('/characters/<string:alias>', methods=['DELETE'])
def delete_character(alias):
    character = db.session.get(Character, alias)
    if not character:
        return {"error": "Character not found"}, 404

    db.session.delete(character)
    db.session.commit()
    return {"message": f"Character '{alias}' deleted."}, 200

def format_character(character):
    return {
        'alias': character.alias,
        'name': character.name,
        'level': character.level,
        'health': character.health,
        'strength': character.strength,
        'defense': character.defense,
        'speed': character.speed
    }
