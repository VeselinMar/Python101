import random

from game_db import quiz_db
from quiz_game.functions import list_topics, get_wrong_answers, print_result

print("Welcome to Quiz Game")

# get topics
topics = []
while not topics:
    topics = input(f'You can choose to play a quiz from the following topics: \n{list_topics(quiz_db)}' 
                   f'\nYou can choose more than one '
                   f'but please choose them by writing the full names of the topics separated by spaces: ').split(' ')
    for topic in topics:
        if topic not in list_topics(quiz_db):
            topics = []
            print('Invalid topic. Please try again.')

# get number of questions to be asked
questions = 0
while questions == 0:
    try:
        questions = int(input("How many questions would you like to try answering: "))
    except ValueError as e:
        print("Sorry, I didn't understand that. Please provide a number.")

count = 0
points = 0

# Keep track of already asked questions
asked_questions = set()

# Main game logic
while count < questions:
    count += 1
    clean_question = False
    while not clean_question:
        topic = topics[random.randint(0, len(topics) - 1)]

        question = random.choice(list(quiz_db[topic].keys()))
        if question not in asked_questions:
            asked_questions.add(question)
            clean_question = True

    # Get the correct answer
    correct_answer = quiz_db[topic][question]

    # Get 3 wrong answers
    other_answers = get_wrong_answers(question ,correct_answer, topic, quiz_db)
    wrong_answers = random.sample(other_answers, min(3, len(other_answers)))

    options = wrong_answers + [correct_answer]

    random.shuffle(options)

    option_labels = ['a', 'b', 'c', 'd']
    labeled_options = dict(zip(option_labels, options))

    print(f'\nTopic: {topic}')
    print(f'Question: {question}')
    for label in labeled_options:
        print(f'\t{label}: {labeled_options[label]}')


    user_answer = input(f'Your choice (a, b, c, d):').lower().strip()

    if labeled_options.get(user_answer) == correct_answer:
        points += 1
        print(f'Yes! {correct_answer} is the correct answer!')
    else:
        print(f'Sorry! The correct answer is: {correct_answer}')

print_result(points, questions)