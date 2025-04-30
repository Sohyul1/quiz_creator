# For Assignment 10: Quiz

# Import random and colorama 
import random
from colorama import Fore, Style, init
init(autoreset=True)

# Open the file to read
with open("quiz_questions.txt", "r") as file:
    lines = file.readlines()

# Make a list for the questions
questions_and_choices = []
line_count = 0 # Line counter
while line_count < len(lines):
    # Extract the questions and choices
    if lines[line_count].startswith("Question:"):
        # Extract the questions and answer line by line
        question_text = lines[line_count].strip()
        choice_a = lines[line_count+1].strip()
        choice_b = lines[line_count+2].strip()
        choice_c = lines[line_count+3].strip()
        choice_d = lines[line_count+4].strip()
        correct_answer = lines[line_count+5].strip(".").replace("Answer:", "").strip()
        # Append the lines into the list
        questions_and_choices.append((question_text, [choice_a, choice_b, choice_c, choice_d], correct_answer))
    line_count += 6
while True:   
    # Get a random question on that file 
    random.shuffle(questions_and_choices)

    # Initialize the score
    score = 0

    # Ask the user the questions
    for current_quest in questions_and_choices:
        print(Style.BRIGHT + Fore.CYAN + "\n" + current_quest[0] + "\n") # Question text
        for choices in current_quest[1]:
            print(Style.BRIGHT + Fore.MAGENTA + choices)

        # Enter their answer
        while True:
            try:
                ans = input(Style.BRIGHT + Fore.CYAN + "\nEnter your answer[A/B/C/D]: ").strip().upper()
                if ans in ["A", "B", "C", "D"]:
                    break
                else:
                    print(Style.BRIGHT + Fore.RED + "Invalid input. Please enter A, B, C, or D.") 
            except ValueError:            
                    print(Style.BRIGHT + Fore.RED + "Oops! Something went wrong. Please try again.")
        
        # Reveal  if he got the right answer
        if ans.upper() == current_quest[2]:  
            print(Style.BRIGHT + Fore.GREEN + "\nCorrect!")
            score += 1
            print(Style.BRIGHT + Fore.GREEN + f"Current score: {score}")
        else:
            print(Style.BRIGHT + Fore.RED  + f"\nIncorrect. The correct answer is {current_quest[2]}.")
            print(Style.BRIGHT + Fore.RED + f"Current score: {score}\n")

    # Reveal final score
    print(Style.BRIGHT + Fore.MAGENTA  + f"\nQuiz completed!\nYour final score: {score}/{len(questions_and_choices)}")

    # Ask if the user wants to play again, with error handling
    while True:
        try:
            retry = input(Style.BRIGHT + Fore.CYAN + "\nWould you like to play again (yes/no)? ").strip().lower()
            if retry in ["yes", "no"]:
                break
            else :
                print(Style.BRIGHT + Fore.RED + "Please enter either 'yes' or 'no'")
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "Oops! Something went wrong. Please try again.")
        
    if retry == "no":
        print("\nThank you for taking the quiz! Goodbye!")
        break