from clear_screen import clear_screen

class Quiz:
    def __init__(self, question_list: list, level: str):
        self.score = 0
        self.question_num = 0
        self.question_list = question_list
        self.level = level
        self.user_answers = []

    def start_quiz(self):
        """Runs the quiz loop."""
        print("=" * 20)
        print(f" {self.level.capitalize()} mode")
        print("=" * 20)

        while self.question_num < len(self.question_list):
            question = self.question_list[self.question_num]
            self.display_question(question)

            user_answer = input("\nYour answer: ").lower()
            self.user_answers.append(user_answer)

            if user_answer == question.answer:
                self.score += 1

            clear_screen()
            self.question_num += 1

        print(f"Your total Score is {self.score}/{len(self.question_list)}")
        self.quiz_summary()

    def display_question(self, questions):
        """Displays a single question and its options."""
        print(f"\nQuestion {self.question_num + 1}: {questions.question}")
        for key, value in questions.option.items():
            print(f"{key}) {value}")

    def quiz_summary(self):
        """Displays a summary of the quiz results."""
        print("\n=== Quiz Summary ===")
        for i, question in enumerate(self.question_list):
            self.display_summary_question(i, question)

    def display_summary_question(self, index, question):
        """Displays one question with correct/wrong marking."""
        print(f"\nQuestion {index + 1}: {question.question}")
        for key, value in question.option.items():
            print(f"  {key}) {value}")

        user_answer = self.user_answers[index]
        correct_answer = question.answer

        if user_answer == correct_answer:
            print(f"\n✅ Your answer: {user_answer} (CORRECT)")
        else:
            print(f"\n❌ Your answer: {user_answer} (WRONG)")
            print(f"✅ Correct answer: {correct_answer}")


