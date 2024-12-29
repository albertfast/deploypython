# Try-except block to handle keyboard interrupt (Ctrl + C) gracefully
try:
    # Loop to perform the operation 3 times
    for i in range(3):
        # Ask the user for the type of operation (either addition or subtraction)
        while True:  # Loop until a valid operator is entered
            print("\nWhich calculation would you like to do [+ or -] [CTRL-C to exit]?")
            choice = input("Enter + or - : ")
            if choice in ["+", "-"]:  # Only accept + or -
                break  # Exit loop if valid input
            else:
                print(
                    "Invalid choice, please enter either + or -"
                )  # Ask again for valid input

        # Get the first number from the user with input validation
        while True:
            try:
                i1 = int(input("Give the first number: "))  # Convert input to integer
                break  # If successful, exit the loop
            except ValueError:
                print(
                    "Invalid input! Please enter a valid number."
                )  # If input is not valid, ask again

        # Get the second number from the user with input validation
        while True:
            try:
                i2 = int(input("Give the second number: "))  # Convert input to integer
                break  # If successful, exit the loop
            except ValueError:
                print(
                    "Invalid input! Please enter a valid number."
                )  # If input is not valid, ask again

        # Perform the calculation based on the operator
        if choice == "+":
            correct_answer = i1 + i2  # Calculate the correct result for addition
            user_answer = int(input(f"{i1} + {i2} = "))  # Ask the user for their answer
        elif choice == "-":
            correct_answer = i1 - i2  # Calculate the correct result for subtraction
            user_answer = int(input(f"{i1} - {i2} = "))  # Ask the user for their answer

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Good work – your answer is correct!")
        else:
            print(f"Nice job, but a better answer is {correct_answer}.")

    print("\nAll 3 calculations are complete!")

# Handle the Ctrl + C action (KeyboardInterrupt)
except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting the program...")
