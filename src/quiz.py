import os

class Quiz:
    def __init__(self, question_list, level):
        self.score = 0
        self.question_num = 0
        self.question_list = question_list
        self.level = level
 
    def start_quiz(self):
        print("=" * 20)
        print(f" {self.level} mode")
        print("=" * 20)
            
        while self.question_num < len(self.question_list):
            question = self.question_list[self.question_num]
            
            print(f"\nQuestion {self.question_num + 1}: {question.question}")
            for key, value in question.option.items():
                print(f"{key}) {value}")
            
            
            user_answer = input("\nYour answer: ").lower()
            
            if user_answer == question.answer:
                self.score += 1
            
        
            clear_screen()
            self.question_num +=1
            
        print(f"Your total Score is {self.score}/10")
            
   
def clear_screen():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')