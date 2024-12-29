for i in range(3):  # Since we have 3 questions, we loop 3 times
    if i == 0:
        # First question
        user_input1 = input("101 + 200 = ")
        if user_input1 == 301:
            print("Good work – your answer is correct!\n")
        else:
            print(f"Nice try, but a better answer is {101 + 200}.\n")
    
    elif i == 1:
        # Second question
        user_input2 = input("100 - (-29) = ")
        if user_input2 == str(100 - (-29)):
            print("Good work – your answer is correct!\n")
        else:
            print(f"Nice try, but a better answer is {100 - (-29)}.\n")
    
    elif i == 2:
        # Third question
        user_input3 = input("-122 + 22 = ")
        if user_input3 == str(-122 + 22):
            print("Good work – your answer is correct!\n")
        else:
            print(f"Nice try, but a better answer is {-122 + 22}.\n")

print("All calculations are complete!")
