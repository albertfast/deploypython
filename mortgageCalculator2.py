# ================================UMPIRE=========================================================
# Understand:
# The program extends the logic of mortgageCalculator1 to calculate the monthly 
# mortgage payment. However, instead of printing the output to the console, 
# the results are written to a file named mortgageOutput.txt.
#
# Functionality:
# 1. The input (amount borrowed, interest rate, and payback period) is displayed 
#    in the console for the user to provide valid inputs.
# 2. The calculated output (monthly payment) along with input echoes is saved 
#    into mortgageOutput.txt for record purposes.
#
# Input Details:
# - Borrowed amount: Whole number (integer).
# - Annual interest rate: Percentage (float).
# - Payback period: Whole number in years (integer).
#
# Output Requirements:
# 1. Input echoes (amount borrowed, interest rate, and payback period) should be 
#    written into the mortgageOutput.txt file.
# 2. Monthly payment should also be included in the file, formatted to two decimal 
#    places (e.g., 1000.00).
# 3. The console should display only the input prompts and nothing else.

# Example:                    Input (Console):                  Output (File):
#               - Amount borrowed: 270000                 - Amount borrowed: 270000
#               - Annual interest rate: 5.125             - Annual interest rate: 5.125
#               - Payback period: 30 years                - Payback period: 30 years
#                                                         - Monthly payment: 1470.11

# Restriction:
# - Inputs must be valid numbers (floats or integers).
# - Borrowed amount must be positive.
# - Annual interest rate and payback period must also be positive.
# - The program must save all results to mortgageOutput.txt and not display 
#   them in the console.

# Match:
# - Input: Borrowed amount (integer), interest rate (float), payback period (integer).
# - Output: Results (input echoes and monthly payment) written to a file.
# - Tools: Python open function for file operations, try-except for error handling.

# Plan:
# 1. Import the calculate_mortgage function from mortgageCalculator1.py.
# 2. Call calculate_mortgage to perform the mortgage calculations and return the result as a string.
# 3. Open a file named mortgageOutput.txt in write mode.
# 4. Write the result to the file while ensuring proper error handling.
# 5. Ensure the program runs smoothly without displaying the results in the console.

# Implementation:

from mortgageCalculator1 import calculate_mortgage  # Importing the calculation logic

def main():
    """
    This program calculates the monthly mortgage payment by calling the `calculate_mortgage`
    function from `mortgageCalculator1.py` and writes the result to `mortgageOutput.txt`.
    """

    # Call the calculate_mortgage function to perform calculations
    # Inputs will be prompted to the user and returned in the result string
    result = calculate_mortgage()

    # Define the name of the output file
    output_file = "mortgageOutput.txt"

    # Write the result to the output file
    try:
        with open(output_file, "w") as file:
            # Writing the result to the file
            file.write(result)
        # Uncomment the next line for debugging (optional)
        # print(f"Results have been successfully written to '{output_file}'.")
    except Exception as e:
        # Error handling for file write operations
        print(f"Error writing to file: {e}")

# Ensure the program runs only when executed directly
if __name__ == "__main__":
    main()

