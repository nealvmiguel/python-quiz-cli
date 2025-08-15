import json

class Question:
    
    def __init__(self, level: str, question: dict, option: str, answer: str):
        self.level = level
        self.question = question
        self.option = option
        self.answer = answer
        

def open_question_json(path):
    
    try:
        with open(path ,'r') as file:
            question_data = json.load(file)
                
        return question_data
    except FileNotFoundError as e :
        print(f"Error: Questions file not found at {e}")
        print("Please make sure the questions.json file exists in the correct location.")
        

        
def if_has_questions(questions):
         # Check if questions loaded successfully
    if questions is None:
        print("Cannot start quiz without questions file.")
        return
            
        
    
    