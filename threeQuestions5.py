# Loop through the range of 3 (since we have 3 questions)
for i in range(3):
    # Based on the value of 'i', assign different questions and correct answers
    if i == 0:
        # First question
        question = "101 + 200 = "
        correct_answer = 101 + 200
    elif i == 1:
        # Second question
        question = "100 - (-29) = "
        correct_answer = 100 - (-29)
    elif i == 2:
        # Third question
        question = "-122 + 22 = "
        correct_answer = -122 + 22

    # A while loop to ensure the user enters a valid input
    while True:
        # Prompt the user with the current question
        user_input = input(question)
        
        # Check if the input is a valid integer (either positive or negative)
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            # If the input matches the correct answer (convert correct answer to string for comparison)
            if user_input == str(correct_answer):
                print("Congratulations – your answer is correct!\n")
                break  # Exit the while loop as the answer is correct
            else:
                # If the answer is incorrect, provide feedback and move to the next question
                print(f"Nice try, but the correct answer is {correct_answer}.\n")
                break  # Exit the while loop and proceed to the next question
        else:
            # If the input is not a valid number, display an error message and prompt again
            print(f"'{user_input}' is an invalid input! Please enter a valid number.\n")

# After all questions are completed, display a final message
print("All calculations are complete!")
