# List of math questions and their correct answers
questions = [
    ("101 + 200", 301),
    ("100 - 29", 71),
    ("122 + 22", 144)
]


# Loop through each question
for question, correct_answer in questions:
    while True:  # Loop until the user provides valid input
        try:
            # Ask the user for their answer
            user_input = int(input(f"{question} = "))

            # Check if the user's answer is correct
            if user_input == correct_answer:
                print("Good work – your answer is correct!\n")
            else:
                print(f"Nice job, but a better answer is {correct_answer}.\n")
            break  # Exit the loop once the question is answered
        except ValueError:
        # Handle invalid input if the user enters non-numeric input
        print("Invalid input! Please enter a valid number.\n")

print("All questions have been answered!")


