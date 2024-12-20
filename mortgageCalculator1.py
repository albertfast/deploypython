# ================================UMPIRE========================================
# Understand:
# The program calculates the monthly mortgage payment based on:
# 1. The borrowed amount (p) entered as a whole number (integer).
# 2. The annual interest rate, entered as a percentage (float).
# 3. The payback period, entered in years (integer).
#
# Formula:
# (p * (1 + r)^n * r) / ((1 + r)^n - 1)
# - p is the principal amount borrowed.
# - r is the monthly decimal interest rate (annual_rate / 12 / 100).
# - n is the total number of monthly payments (years * 12).
#
# Output Requirements:
# 1. Display the borrowed amount, annual interest rate, and payback period as entered.
# 2. Display the calculated monthly payment as a floating-point number formatted to 2 decimal places.

# Example:                    Input:                                Output:
#               - Amount borrowed: 270000                     - Amount borrowed: $270000
#               - Annual interest rate: 5.125                 - Annual interest rate: 5.125
#               - Payback period: 30 years                    - Payback period in years: 30
#                                                             - Monthly payment: $1470.11

# Restriction:
# - Inputs must be valid numbers (floats or integers).
# - Borrowed amount must be a positive whole number.
# - Annual interest rate must be a positive number.
# - Payback period must be a positive number in years.
# - Use math library for calculations.
# - Use the math.pow() function or the ** operator for exponentiation. Do not use both.

# Match:
# - Input: Borrowed amount (integer), interest rate (float), payback period (integer).
# - Output: Display input echoes and the monthly payment calculation.
# - Tools: Python math module, formatted strings for output.

# Plan:
# 1. Define a function calculate_mortgage that takes three parameters: p (borrowed amount),
#    annual_rate (interest rate), and years (payback period).
# 2. Validate the inputs inside the function or in the main program.
# 3. Convert the annual interest rate to a monthly rate (r = annual_rate / 12 / 100).
# 4. Calculate the total number of payments (n = years * 12).
# 5. Use the mortgage payment formula to calculate the monthly payment.
# 6. Format the result to 2 decimal places and return or print the required outputs.

# Implementation:

import math

def calculate_mortgage(p=None, annual_rate=None, years=None, standalone=False):
    """
    This function calculates the monthly mortgage payment based on the borrowed amount,
    annual interest rate, and payback period (in years). It can print the results or return them as a string.

    Parameters:
    - p: The amount borrowed (float). If None, the user is asked to input it.
    - annual_rate: The annual interest rate (float). If None, the user is asked to input it.
    - years: The payback period in years (int). If None, the user is asked to input it.
    - standalone: If True, the result is printed to the debug screen. If False, it returns the result as a string.

    Returns:
    - A formatted string with the calculated results.
    """

    # Function to get valid user input as a float
    # We use float for all inputs so we can handle both integers and decimals
    def get_valid_input(prompt):
        while True:  # Keep asking until the user provides a valid input
            user_input = input(prompt)  # Ask the user for input
            if user_input.lower() == 'exit':  # Allow the user to exit the program
                print("\nExiting the program. Goodbye!")
                exit()
            try:
                return float(user_input)  # Try to convert the input to a float
            except ValueError:  # Handle invalid input
                print("Invalid input! Please enter a valid number or type 'exit' to quit.")

    # Ask the user for inputs if they are not provided as function arguments
    if p is None:  # Check if the borrowed amount is not provided
        p = get_valid_input("What's the amount borrowed: ")  # Ask the user to input it
    if annual_rate is None:  # Check if the annual interest rate is not provided
        annual_rate = get_valid_input("What's the annual interest rate: ")  # Ask the user to input it
    if years is None:  # Check if the payback period is not provided
        years = get_valid_input("What's the payback period (in years): ")  # Ask the user to input it

    # Convert the annual interest rate to a monthly interest rate
    r = annual_rate / 100 / 12

    # Calculate the total number of months for the mortgage
    n = years * 12

    # Calculate the monthly mortgage payment using the mortgage formula
    monthly_payment = (p * math.pow((1 + r), n) * r) / (math.pow((1 + r), n) - 1)

    # Prepare the formatted result as a string
    # Borrowed amount and payback period are converted to integers for a cleaner output
    result = (
        f"Amount borrowed: ${int(p)}\n"  # Borrowed amount as an integer
        f"Annual interest rate: {annual_rate}\n"  # Interest rate as a float
        f"Payback period in years: {int(years)}\n"  # Payback period as an integer
        f"Monthly payment = ${monthly_payment:.2f}"  # Monthly payment as a float with 2 decimal places
    )

    # If standalone is True, print only the monthly payment to the debug screen
    if standalone:
        print(f"\nMonthly payment (calculated output) = ${monthly_payment:.2f}")

    # Return the formatted result as a string
    return result

# If the script is run directly, execute the standalone functionality
if __name__ == "__main__":
    calculate_mortgage(standalone=True)
