# The degree symbol (°) is represented by the Unicode character '\u00B0'
degree_symbol = "\u00B0"  # This will be used to display the ° symbol after temperature values

# Loop to perform the temperature conversion exactly 10 times
for i in range(1, 11):  # Loop runs 10 times for 10 temperature inputs
    # Infinite loop to ensure we get valid user input
    while True:
        # Prompt the user for a temperature in Celsius
        temperature_celsius = input("Enter temperature in Celsius: ")

        # Check if the input is a valid float number (can contain a plus or minus sign or decimal point)
        # Remove any decimal point and plus/minus sign before checking if the remaining string is numeric
        if temperature_celsius.replace('.', '', 1).replace('+', '', 1).replace('-', '', 1).isdigit():
            # If the input is valid, convert it to a float
            temperature_celsius = float(temperature_celsius)
            break  # Exit the loop if a valid input is provided
        else:
            # If the input is not valid, show an error message and repeat the prompt
            print("Invalid input! Please enter a valid number. \n")

    # Convert the Celsius temperature to Fahrenheit using the formula: F = (C * 9/5) + 32
    temperature_fahrenheit = (9 / 5) * temperature_celsius + 32

    # Print the result of the conversion with 1 decimal place precision
    # The ° symbol and "C" or "F" are appended to indicate Celsius or Fahrenheit
    print(f"{i}. The temperature in degrees {temperature_celsius:}{degree_symbol}C is equal to {temperature_fahrenheit:.1f}{degree_symbol}F.\n")

# Once all 10 conversions are done, print the completion message
print("All 10 temperatures have been converted!")
