# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = "\u00B0"  # This will be used to display the ° symbol after temperature values

try:
    for i in range(10):  # The loop runs 10 times, converting 10 different temperatures from Celsius to Fahrenheit
        while True:  # Infinite loop to ensure that valid input is received
            try:
                t = input(f"Enter temperature in Celsius [CTRL-C to exit]: ")
                C = float(t)  # Convert the input string to a float

                F = (9 / 5) * C + 32
                # Print the Celsius input and the Fahrenheit conversion
                print(f"The temperature in degrees C is {C:.1f}{degree_symbol}, which is {F:.1f}{degree_symbol} Fahrenheit.\n")
                break  # Exit the loop once conversion is successful
            except ValueError:
                # Handle invalid number input
                print(f"'{t}' is an invalid input! Please enter a valid numeric value for temperature.\n")

    print("All 10 temperatures have been converted!")

except KeyboardInterrupt:
    # Catch the CTRL-C interrupt and print a message
    print("\nConversion interrupted by user. Exiting the program gracefully...")
