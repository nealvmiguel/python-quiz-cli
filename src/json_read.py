import json


def open_json(path, level):
    
    
    with open(path, 'r') as file:
        data = json.load(file)
    
    
    if level == 'easy' and level in data:
        print("===========================")
        print(f" {level} mode")
        print("===========================")
        process_quiz_data(data,level)
    
    if level == 'medium' and level in data:
        print("===========================")
        print(f" {level} mode")
        print("===========================")
        process_quiz_data(data,level)
            
    if level == 'hard' and level in data:
        
        print("===========================")
        print(f" {level} mode")
        print("===========================")
  
    
        
        
        

def process_quiz_data(data,level) -> None:
    """
    Process quiz questions and calculate the score

    Args:
        data (json): _description_
        level (string): _description_
    """
    
    score = 0
    current_index = 0
    questions = data[level]
    user_answers = []

    while current_index < len(questions):
        question= questions[current_index]
        
        print(f"\nQuestion {current_index + 1}: {question['question']}")
        
        for key, value in question['options'].items():
            print(f"  {key}) {value}")
            
        user_input_answer = input("\nAnswer: ")
        
  
        
        user_answers.append(user_input_answer)
        if user_input_answer == question['answer']:
            score += 1
            
        clear_screen()
        current_index += 1
        
     
    print(f"Your total score is {score}/{len(questions)}")
    
    quiz_summary(user_answers, questions)
    
    
    
           
def quiz_summary(user_answers, questions) -> None:
    for i, question  in enumerate(questions):
        user_answer = user_answers[i]
        correct_answer = question['answer']
            
        print(f"\nQuestion {i+1}: {question['question']}")
            
        for key, value in question['options'].items():
            print(f"  {key}) {value}")
            
        if user_answer == correct_answer:
            print(f"]\n✅ Your answer: {user_answer} (CORRECT)")
        else:
            print(f"\n❌ Your answer: {user_answer} (WRONG)")

 

def clear_screen():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')