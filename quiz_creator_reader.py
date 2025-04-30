# For Assignment 10: Quiz

# Import random
import random

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
        correct_answer = lines[i+5].strip()
        # Append the lines into the list
        questions.append((question_text, [choice_a, choice_b, choice_c, choice_d], correct_answer))
    i += 6
    
# Get a random question on that file 
random.shuffle(questions)

# Initialize the score
score = 0

# Ask the user the questions
for current_quest in questions:
    print(current_quest[0]) # Question text
    for choices in current_quest[1]:
        print(choices)

    # Enter their answer
    ans = input("Enter your answer: ").strip().upper()

# Reveal  if he got the right answer
    if ans == current_quest[2]:  
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {current_quest[2]}.\n")

# Reveal final score
print(f"Quiz completed! Your final score: {score}/{len(questions)}")
