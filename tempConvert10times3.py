# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = "\u00B0"  # This will be used to display the ° symbol after temperature values
try:
    # For loop to perform the conversion exactly 10 times
    for i in range(10):  # Loop through 10 times to convert 10 temperatures
        while True:  # Infinite loop to continuously ask for valid input
            try:
                # Prompt the user to input the temperature in Celsius
                # 'end=""' ensures the input is on the same line as the prompt
                print(f"Enter temperature in Celsius [CTRL-C to exit]: ", end="")
                
                # Capture the user input into 't' and attempt to convert it to a floating-point number
                t = input()  # Take the input as a string
                C = float(t)  # Convert the string input to a floating-point number
                
                # Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
                F = (9/5) * C + 32

                # Print the result with the modified output format
                # Example: The temperature in degrees 5 F° is 41.0° Fahrenheit
                print(f"The temperature in degrees {t} F{degree_symbol} is {F:.1f}{degree_symbol} Fahrenheit\n")
                
                # Break out of the while loop once valid input is provided and the conversion is done
                break
            except ValueError:  # Handle the case where the input is not a valid number
                # Print an error message indicating the input was invalid
                print(f"'{t}' Invalid input! Please enter a valid numeric value for temperature.\n")
    
    # Once all 10 conversions are done, print a message indicating completion
    print("All 10 temperatures have been converted!")

# Handle the Ctrl + C action (KeyboardInterrupt)
except KeyboardInterrupt:
    # This block catches the keyboard interruption if the user presses Ctrl + C
    # It ensures the program doesn't crash and exits gracefully with a friendly message
    print("\nConversion interrupted by user. Exiting the program...")
