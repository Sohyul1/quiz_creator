# For Assignment 9: Quiz Creator

# Initialize by opening a file 
file = open("quiz_questions.txt", "a")

# Start of loop
while True:
    # Ask for user input (question)
    questn = input("Enter the question you like: \n")

    # Ask for user input (answer)
    a = input("Letter 'A' value: \n")
    b = input("Letter 'B' value: \n")
    c = input("Letter 'C' value: \n")
    d = input("Letter 'D' value: \n")

    # Ask the user for the right answer
    right_ans = input("Letter of the right answer (A/B/C/D): \n")
    while True:
        right_ans = input("Letter of the right answer (A/B/C/D): \n").strip().upper()
        if right_ans in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    
    # Write the collected data into text file
    file.write("Question: " + questn + "\n")
    file.write("A. " + a + "\n")
    file.write("B. " + b + "\n")
    file.write("C. " + c + "\n")
    file.write("D. " + d + "\n")
    file.write("Answer: " + right_ans.upper() + "\n")
    file.write("\n")

     # Make a loop to keep asking for input
    again = input("Add another question? (yes/no): \n").strip().lower()
    if again != 'yes':
        print("Quiz creation completed!")
        break

    # Close the file once done
    file.close()
