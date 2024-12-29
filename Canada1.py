# Loop continuously to allow the user to perform multiple conversions or quit
while True:
    # Prompt the user to input the temperature in Celsius or 'Q' to quit
    print("Enter a temperature in Celsius or 'Q' to quit: ", end="")

    # Get user input
    user_input = input()

    # Check if the user wants to quit
    if user_input.lower() == 'q':  # Check if the input is 'q' (case insensitive)
        print("Goodbye!")
        break  # Exit the loop and end the program

    # If the user enters a valid number, proceed with the conversion
    try:
        C = float(user_input)  # Try to convert the input to a floating-point number
        # Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32
        F = (9/5) * C + 32

        # Print the Celsius and Fahrenheit values with 1 decimal place for comparison
        print(f"{C} Celsius equals {F:.1f} Fahrenheit\n")

    # Handle invalid input (e.g., non-numeric values except 'Q')
    except ValueError:
        print("Invalid input. Please enter a valid temperature in Celsius or 'Q' to quit.\n")
