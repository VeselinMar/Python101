import importlib.util
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "game_db.py")

def list_topics(db):
    keys = list(db.keys())
    return '\n'.join(keys)

def get_wrong_answers(current_question, correct_answer, topic, db):
    return [
        answer for question,
        answer in db[topic].items()
        if question != current_question
        and answer != correct_answer
    ]

def print_result(points, questions):
    if points > questions * 0.75:
        print(f'\nGood Job You answered {points} question(s) out of {questions} questions.')
    else:
        print(f'\nYou answered {points} question(s) out of {questions} questions. You can do better, why not try again?')

# --------------------------
# Database Editing Functions
#---------------------------

def load_db():
    spec = importlib.util.spec_from_file_location("game_db", FILE_PATH)
    game_db = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(game_db)
    return game_db.quiz_db

def save_db(db):
    with open(FILE_PATH, "w") as f:
        f.write("quiz_db = ")
        f.write(repr(db))

def add_question(topic, question, answer):
    db = load_db()
    if topic not in db:
        db[topic] = {}
    db[topic][question] = answer
    save_db(db)
    print(f"✅ Added question to {topic}")

def remove_question(topic, question):
    db = load_db()
    if topic in db and question in db[topic]:
        del db[topic][question]
        save_db(db)
        print(f"✅ Removed question from {topic}")
    else:
        print("⚠️ Question not found.")

def add_topic(topic, questions=None):
    db = load_db()
    if topic not in db:
        db[topic] = questions or {}
        save_db(db)
        print(f"✅ Added topic {topic}")
    else:
        print("⚠️ Topic already exists.")