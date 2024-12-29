# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = "\u00B0"  # This will be used to display the ° symbol after temperature values

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
        F = 9/5 * C + 32

        # Round both the Celsius and Fahrenheit values to integers for a cleaner output
        C_rounded = round(C)  # Rounding Celsius value to the nearest integer
        F_rounded = round(F)  # Rounding Fahrenheit value to the nearest integer

        # Print the result with the degree symbol, showing rounded values
        print(f"{C_rounded}{degree_symbol}C is {F_rounded}{degree_symbol}F\n")

    # Handle invalid input (e.g., non-numeric values except 'Q')
    except ValueError:
        print("Invalid input. Please enter a valid temperature in Celsius or 'Q' to quit.\n")
