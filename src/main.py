import os

from quiz import Quiz, clear_screen
from question_model import Question, open_question_json


def main():
    print("===========================")
    print("Welcome to the python quiz app\nPlease choose a difficulty")
    print("===========================")
    
    path = os.path.join(os.path.dirname(__file__),'..', 'data', 'questions.json')
    questions = open_question_json(path)
    
    if questions is None:
        print("Cannot start quiz without questions file.")
        return False
        
    question_list = []
    
    
    while True:
        level = input("Easy, Medium or Hard\nInput: ").lower()
        lvl = questions.keys()
        
        if level in lvl:
            break
        
        else:
            clear_screen()
            print("Not a valid Level")
            main()
            
    
    for question in questions[level]:
        question_text = question['question']
        question_option = question['options']
        question_answer = question['answer']
        new_question = Question(level, question_text, question_option, question_answer)
        question_list.append(new_question)
    
     
    quiz = Quiz(question_list, level)
    
    clear_screen()
    quiz.start_quiz()
    
    retry = input("\nWanna go again? Yes / No: ").lower()
    
    if retry == "yes":
        clear_screen()
        main()
    else:
        print("Okay come again")
    
    
    
    

    
    


    
    

    



if __name__ == "__main__":
    main()
    