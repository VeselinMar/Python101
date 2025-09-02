import random
from game_db import quiz_db
from functions import (
    list_topics, get_wrong_answers, print_result,
    add_question, remove_question, add_topic, load_db
)

def play_quiz():
    db = load_db()
    print("Welcome to Quiz Game")

    # get topics
    topics = []
    while not topics:
        topics = input(
            f'You can choose to play a quiz from the following topics: \n{list_topics(db)}'
            f'\nYou can choose more than one, separated by spaces: '
        ).split(' ')
        for topic in topics:
            if topic not in db:
                topics = []
                print('Invalid topic. Please try again.')

    # get number of questions
    questions = 0
    while questions == 0:
        try:
            questions = int(input("How many questions would you like to try answering: "))
        except ValueError:
            print("Sorry, I didn't understand that. Please provide a number.")

    count = 0
    points = 0
    asked_questions = set()

    while count < questions:
        count += 1
        clean_question = False
        while not clean_question:
            topic = random.choice(topics)
            question = random.choice(list(db[topic].keys()))
            if question not in asked_questions:
                asked_questions.add(question)
                clean_question = True

        correct_answer = db[topic][question]
        other_answers = get_wrong_answers(question, correct_answer, topic, db)
        wrong_answers = random.sample(other_answers, min(3, len(other_answers)))

        options = wrong_answers + [correct_answer]
        random.shuffle(options)

        option_labels = ['a', 'b', 'c', 'd']
        labeled_options = dict(zip(option_labels, options))

        print(f'\nTopic: {topic}')
        print(f'Question: {question}')
        for label in labeled_options:
            print(f'\t{label}: {labeled_options[label]}')

        user_answer = input(f'Your choice (a, b, c, d): ').lower().strip()

        if labeled_options.get(user_answer) == correct_answer:
            points += 1
            print(f'✅ Correct! {correct_answer}')
        else:
            print(f'❌ Sorry! The correct answer is: {correct_answer}')

    print_result(points, questions)

def editor_menu():
    while True:
        print("\n--- Quiz Database Editor ---")
        print("1. Add Question")
        print("2. Remove Question")
        print("3. Add Topic")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            topic = input("Enter topic: ").strip()
            q = input("Enter question: ").strip()
            a = input("Enter answer: ").strip()
            add_question(topic, q, a)

        elif choice == "2":
            topic = input("Enter topic: ").strip()
            q = input("Enter question to remove: ").strip()
            remove_question(topic, q)

        elif choice == "3":
            topic = input("Enter new topic name: ").strip()
            add_topic(topic)

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play Quiz")
        print("2. Edit Database")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            editor_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
