import math


def calculate_mortgage(p=None, annual_rate=None, years=30, verbose=True):
    """
    Calculates and prints the mortgage monthly payment.

    Parameters:
    - p: The amount borrowed (float). If None, asks the user.
    - annual_rate: The annual interest rate (float). If None, asks the user.
    - years: The payback period in years (int). Default is 30 years.
    - verbose: Controls the level of output detail (bool). Default is True.

    Returns:
    - A string containing the formatted calculation results for use in other programs.
    """

    # Function to get a valid floating-point input from the user
    def get_valid_float(prompt):
        while True:
            user_input = input(prompt)
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                exit()
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid number or type 'exit' to quit.")

    # Ask the user for inputs with validation
    if p is None:
        p = get_valid_float("What's the amount borrowed: ")
    if annual_rate is None:
        annual_rate = get_valid_float("What's the annual interest rate: ")

    # Convert the annual interest rate to a monthly interest rate
    r = annual_rate / 100 / 12

    # Calculate the total number of months for the mortgage
    n = years * 12

    # Calculate the monthly mortgage payment using the formula
    monthly_payment = (p * math.pow((1 + r), n) * r) / (math.pow((1 + r), n) - 1)

    if verbose:
        # Prepare the detailed formatted result
        result = (
            f"Amount borrowed (programmer input): {int(p)}\n"
            f"Annual interest rate (programmer input): {annual_rate}\n"
            f"Payback period (programmer input): {years}\n"
            f"Monthly payment (calculated output) = {monthly_payment:.2f}\n"
        )
    else:
        # Prepare the concise formatted result
        result = (
            f"Payback period (programmer input): {years}\n"
            f"Monthly payment (calculated output) = {monthly_payment:.2f}\n"
        )

    # Print results for standalone usage
    if __name__ == "__main__":
        print(result)

    # Return results as a string for use in other programs
    return result


# Execute as a standalone program
if __name__ == "__main__":
    calculate_mortgage()
