import os

class Quiz:
    def __init__(self, question_list: list, level: str):
        self.score = 0
        self.question_num = 0
        self.question_list = question_list
        self.level = level
        self.user_answers = []
 
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
            self.user_answers.append(user_answer)
            
            if user_answer == question.answer:
                self.score += 1
            
        
            clear_screen()
            self.question_num +=1
            
        print(f"Your total Score is {self.score}/10")
        
        self.quiz_summary()
        
    def quiz_summary(self):
        
        for i, question in enumerate(self.question_list):
            user_answer = self.user_answers[i]
            correct_answer = question.answer
            
            print(f"\nQuestion {i+1}: {question.question}")
                
            for key, value in question.option.items():
                print(f"  {key}) {value}")
                
            if user_answer == correct_answer:
                print(f"]\n✅ Your answer: {user_answer} (CORRECT)")
            else:
                print(f"\n❌ Your answer: {user_answer} (WRONG)")
                
 
        
            
            
   
def clear_screen():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')