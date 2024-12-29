# Function to ask a math question and check the answer
def ask_question(question, correct_answer):
    user_input = int(input(question))
    if user_input == correct_answer:
        print("Good work – your answer is correct!\n")
    else:
        print(f"Nice job, but a better answer is {correct_answer}.\n")

# Present three addition and subtraction problems
print("Three addition and subtraction problems:")

# Ask three math questions
ask_question("101 + 200 = ", 301)
ask_question("100 - 29 = ", 71)
ask_question("122 + 22 = ", 144)
