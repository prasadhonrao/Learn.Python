import json


def load_db():
    with open("flashcards-db.json") as f:
        return json.load(f)


db = load_db()
