# Try-except block to handle Ctrl + C for graceful exit
try:
    # Loop to give the user 3 chances to provide input
    for _ in range(3):
        while True:
            # Read a grade from the keyboard and convert to lowercase
            grade = input("What is your grade? [A, B, C, D, or F] [CTRL-C to exit] : ").lower()

            # Check for passing or failing grades
            if grade in ['a', 'b', 'c']:
                print("Really excellent work!\n")
                break  # Exit the while loop after a valid input
            elif grade in ['d', 'f']:
                print("Yikes -- you failed...\n")
                break  # Exit the while loop after a valid input
            else:
                print("No, that's an invalid entry. Please try again.\n")  # Re-prompt the user for valid input

# Handle the Ctrl + C action (KeyboardInterrupt)
except KeyboardInterrupt:
    print("\nQuiz interrupted by user. Exiting the program...")
