# For Assignment 9: Quiz Creator

# Start of loop
while True:
    # Ask for user input (question)
    questn = input("Enter the question you like: ")

    # Ask for user input (answer)
    a = input("Letter 'A' value: ")
    b = input("Letter 'B' value: ")
    c = input("Letter 'C' value: ")
    d = input("Letter 'D' value: ")

    # Ask the user for the right answer
    right_ans = input("Letter 0f the right answer: ")
    # Make a loop to keep asking for input
    again = input("Add another question? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Quiz creation completed!")
        

    # Write the collected data into text file