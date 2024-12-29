# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = "\u00B0"  # This will be used to display the ° symbol after temperature values

# Loop continuously to allow the user to perform multiple conversions
while True:
    # Ask the user which conversion they want to perform
    print("What would you like to convert?")
    print("Enter 'F' to convert Fahrenheit to Celsius.")
    print("Enter 'C' to convert Celsius to Fahrenheit.")
    print("Enter 'Q' to quit.")  # Add an option for quitting the program

    # Get the user's choice
    choice = input("Your choice (F/C/Q): ").upper()  # Convert input to uppercase to handle 'f', 'c', and 'q'

    # If the user chooses to convert Fahrenheit to Celsius
    if choice == "F":
        # Prompt the user to input the temperature in Fahrenheit
        print("What's the temperature in Fahrenheit? ", end="")
        F = float(input())  # The input is taken as a floating-point number to allow decimal values

        # Convert Fahrenheit to Celsius using the formula C = 5/9 * (F - 32)
        C = 5/9 * (F - 32)

        # Round both the Celsius and Fahrenheit values to integers for a cleaner output
        C_rounded = round(C)  # Rounding Celsius value to the nearest integer
        F_rounded = round(F)  # Rounding Fahrenheit value to the nearest integer

        # Print the result with the degree symbol, showing rounded values
        print(f"\n{F_rounded}{degree_symbol}F is {C_rounded}{degree_symbol}C\n")

    # If the user chooses to convert Celsius to Fahrenheit
    elif choice == "C":
        # Prompt the user to input the temperature in Celsius
        print("What's the temperature in Celsius? ", end="")
        C = float(input())  # The input is taken as a floating-point number to allow decimal values

        # Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32
        F = 9/5 * C + 32

        # Round both the Celsius and Fahrenheit values to integers for a cleaner output
        C_rounded = round(C)  # Rounding Celsius value to the nearest integer
        F_rounded = round(F)  # Rounding Fahrenheit value to the nearest integer

        # Print the result with the degree symbol, showing rounded values
        print(f"\n{C_rounded}{degree_symbol}C is {F_rounded}{degree_symbol}F\n")

    # If the user chooses to quit
    elif choice == "Q":
        print("Goodbye!")  # Print a goodbye message
        break  # Exit the loop and end the program

    # If the user enters an invalid choice
    else:
        print("Invalid choice! Please enter 'F', 'C', or 'Q'.")
