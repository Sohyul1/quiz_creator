# For Assignment 10: Quiz

# Import random and colorama 
import random
from colorama import Fore, Style, init
init(autoreset=True)

# Open the file to read
with open("quiz_questions.txt", "r") as file:
    lines = file.readlines()

# Make a list for the questions
questions = []
i = 0 # Line counter
while i < len(lines):
    # Extract the questions and choices
    if lines[i].startswith("Question:"):
        # Extract the questions and answer line by line
        question_text = lines[i].strip()
        choice_a = lines[i+1].strip()
        choice_b = lines[i+2].strip()
        choice_c = lines[i+3].strip()
        choice_d = lines[i+4].strip()
        correct_answer = lines[i+5].strip(".").replace("Answer:", "").strip()
        # Append the lines into the list
        questions.append((question_text, [choice_a, choice_b, choice_c, choice_d], correct_answer))
    i += 6
while True:   
    # Get a random question on that file 
    random.shuffle(questions)

    # Initialize the score
    score = 0

    # Ask the user the questions
    for current_quest in questions:
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
                    print("Invalid input. Please enter A, B, C, or D.") 
            except ValueError:            
                    print("Oops! Something went wrong. Please try again.")
        
        # Reveal  if he got the right answer
        if ans.upper() == current_quest[2]:  
            print(Style.BRIGHT + Fore.GREEN + "\nCorrect!")
            score += 1
            print(Style.BRIGHT + Fore.GREEN + f"Current score: {score}")
        else:
            print(Style.BRIGHT + Fore.RED  + f"\nIncorrect. The correct answer is {current_quest[2]}.")
            print(Style.BRIGHT + Fore.RED + f"Current score: {score}\n")

    # Reveal final score
    print(Style.BRIGHT + Fore.MAGENTA  + f"\nQuiz completed! Your final score: {score}/{len(questions)}")

    # Ask if the user wants to play again, with error handling
    while True:
        try:
            retry = input(Style.BRIGHT + Fore.CYAN + "\nWould you like to play again (yes/no)? ").strip().lower()
            if retry in ["yes", "no"]:
                break
            else :
                print("Please enter either 'yes' or 'no'")
        except ValueError:
            print("Oops! Something went wrong. Please try again.")
        
    if retry == "no":
        print("\nThank you for taking the quiz! Goodbye!")
        break