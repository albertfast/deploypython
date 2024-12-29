# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = (
    "\u00B0"  # This will be used to display the ° symbol after temperature values
)

try:
    # For loop to perform the conversion exactly 10 times
    for i in range(10):
        while True:  # Loop until valid input is entered
            try:
                # Prompt the user to input the temperature in Celsius
                print(
                    f"Enter temperature in Celsius [{10 - i} more to go] [CTRL-C to exit]: ",
                    end="",
                )
                C = float(
                    input()
                )  # The input is taken as a floating-point number to allow decimal values

                # Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32
                F = 9 / 5 * C + 32

                # Print the result with the degree symbol, showing values with 1 decimal precision
                print(
                    f"The temperature in degrees F is {F:.1f}{degree_symbol} Fahrenheit\n"
                )
                break  # Exit the loop once valid input is received
            except ValueError:
                print(
                    "Invalid input! Please enter a valid numeric value for temperature."
                )  # Error message for non-numeric input

    print("All 10 temperatures have been converted!")

except KeyboardInterrupt:
    # Handle the Ctrl + C action (KeyboardInterrupt)
    print("\nConversion interrupted by user. Exiting the program...")
