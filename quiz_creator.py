# For Assignment 9: Quiz Creator

# Initialize by opening a file 
file = open("quiz_questions.txt", "a")

# Start of loop
while True:
    # Ask for user input (question)
    questn = input("\nEnter a question: \n")

    # Ask for user input (answer)
    choice_a = input("Letter 'A' value: \n")
    choice_b = input("Letter 'B' value: \n")
    choice_c = input("Letter 'C' value: \n")
    choice_d = input("Letter 'D' value: \n")

    # Ask the user for the right answer
    while True:
        right_ans = input("Letter of the right answer [A/B/C/D]: \n").strip().upper()
        if right_ans in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.\n")
    
    # Write the collected data into text file
    file.write(f"Question: {questn}\n")
    file.write(f"A. {choice_a}\n")
    file.write(f"B. {choice_b}\n")
    file.write(f"C. {choice_c}\n")
    file.write(f"D. {choice_d} \n")
    file.write(f"Answer: {right_ans.upper()} \n")
    file.write("\n")

     # Make a loop to keep asking for input
    again = input("Enter another question? [yes/no]: \n").strip().lower()
    if again.startswith("y"):
        continue
    elif again.startswith("n"):
        print("Quiz creation completed!\n")
        break
    else:
        print("Invalid input. Please type a response that starts with 'y' (yes) or 'n' (no).\n")

# Close the file once done
file.close()
