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
    #extract the questions and choices
    if lines[i].startswith("Question:"):
        

# Get a random question on that file 


# Ask the user the questions


# Reveal the right answer


# Repeat until tehre  are o more questions in the file


# Reveal final score