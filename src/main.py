import os
from quiz import Quiz
from clear_screen import clear_screen
from question_model import Question, open_question_json


def ask_level(available_levels: list) -> str:
    """Prompt the user until they enter a valid difficulty level."""
    while True:
        level = input("Easy, Medium or Hard\nInput: ").lower()
        if level in available_levels:
            return level
        clear_screen()
        print("Not a valid level")


def build_question_list(questions: dict, level: str) -> list:
    """Build a list of Question objects for the given difficulty level."""
    question_list = []
    for question in questions[level]:
        new_question = Question(
            level,
            question['question'],
            question['options'],
            question['answer']
        )
        question_list.append(new_question)
    return question_list


def main():
    # Load questions file
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'questions.json')
    questions = open_question_json(path)

    if questions is None:
        print("Cannot start quiz without questions file.")
        return

    while True:
        # Ask for difficulty level
        clear_screen()
        print("=" * 27)
        print("Welcome to the Python Quiz App")
        print("Please choose a difficulty")
        print("=" * 27)

        level = ask_level(questions.keys())

        # Create question list for this session
        question_list = build_question_list(questions, level)

        # Run quiz
        clear_screen()
        quiz = Quiz(question_list, level)
        quiz.start_quiz()

        # Retry prompt
        retry = input("\nWanna go again? Yes / No: ").lower()
        if retry != "yes":
            print("Okay, come again!")
            break


if __name__ == "__main__":
    main()
