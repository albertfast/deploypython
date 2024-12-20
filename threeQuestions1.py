print("\nThree addition and subtraction problems: \n")
# Loop through the range of 3 (since we have 3 questions)
for i in range(3):   # Based on the value of 'i', assign different questions and correct answers
    if i == 0:
        question = "101 + 200 = " # First question
        correct_answer = 101 + 200
    elif i == 1:
        question = "100 - (-29) = " # Second question
        correct_answer = 100 - (-29)
    elif i == 2:
        question = "-122 + 22 = " # Third question
        correct_answer = -122 + 22
    while True: # A while loop to ensure the user enters a valid input
        # Prompt the user with the current question
        user_input = input(question)
        # Check if the input is a valid number:
        # (1) It is a digit (positive integer),
        # (2) It starts with '-' and the rest are digits (negative integer),
        # (3) It starts with '+' and the rest are digits (positive integer with '+')
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()) or (user_input.startswith('+') and user_input[1:].isdigit()):
            # If the input matches the correct answer (convert correct answer to string for comparison)
            if user_input == str(correct_answer) or user_input == f"+{correct_answer}":  # Adding condition for '+' sign
                print("Good work – your answer is correct!\n")
                break  # Correct answer, exit the loop and move to the next question
            else:
                print(f"Nice job, but a better answer is {correct_answer}.\n")
                break  # Incorrect answer, exit the loop and move to the next question
        else:
            # If the input is not a valid number, display an error message and prompt again
            print(f"'{user_input}' is an invalid input! Please enter a valid number.\n")
# Since all questions are complete
print("All calculations are complete!")
