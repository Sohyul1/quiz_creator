# For Assignment 10: Quiz

# Import random
import random

# Open the file to read
with open("quiz_questions.txt", "r") as file:
    lines = file.readlines()

# Make a list for the questions
questions = []
i = 0 # Line counter
while i < len(questions):
    # Extract the questions and choices
    if lines[i].startswith("Question:"):
        # Extract the questions and answer line by line
        question_text = lines[i]
        choice_a = lines[i+1]
        choice_b = lines[i+2]
        choice_c = lines[i+3]
        choice_d = lines[i+4]
        correct_answer = lines[i+5]
        # Append the lines into the list
        questions.append((question_text, [choice_a, choice_b, choice_c, choice_d], correct_answer))
    i += 6
    
# Get a random question on that file 
random.shuffle(questions)

# Ask the user the questions


# Reveal the right answer


# Repeat until tehre  are o more questions in the file


# Reveal final score