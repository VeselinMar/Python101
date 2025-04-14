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
