import os

from json_read import open_json, clear_screen;

path = os.path.join(os.path.dirname(__file__),'..', 'data', 'questions.json')

def main():
    print("===========================")
    print("Welcome to the python quiz app\nPlease choose a difficulty")
    print("===========================")
    level = input("Easy, Medium or Hard\nInput: ")
    clear_screen()
    open_json(path, level)
    
if __name__ == "__main__":
    main()
    