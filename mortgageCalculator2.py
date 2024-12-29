#Programming Concepts In Python by Robert Burns Exercises 5.1	A Simple Mortgage Calculator, v.2.0

def calculate_mortgage():
    # Get the amount borrowed from the user as a floating-point number
    p = float(input("What's the amount borrowed? "))
    
    # Get the annual interest rate from the user as a floating-point number
    annual_rate = float(input("What's the annual interest rate? "))
    
    # Get the payback period in years from the user as an integer
    years = int(input("Payback period in years? "))

    # Convert the annual interest rate to a monthly interest rate by dividing by 12 months and 100 (to get the percentage)
    r = annual_rate / 100 / 12
    
    # Calculate the total number of months for the mortgage (years * 12)
    n = years * 12

    # Calculate the monthly mortgage payment using the mortgage payment formula
    # Formula: M = P * (r(1 + r)^n) / ((1 + r)^n - 1)
    mortgageMontlyPayment = (p * (1 + r) ** n * r) / ((1 + r) ** n - 1)

    # Calculate the total payment over the life of the mortgage (monthly payment * number of months)
    t = mortgageMontlyPayment * n

    # Print the input and calculated values
    # Amount borrowed, formatted to two decimal places with commas for large numbers (e.g., $150,000.00)
    print(f"Amount borrowed (user input) = ${p:,.2f}")
    
    # Annual interest rate, formatted to three decimal places
    print(f"Annual interest rate (user input) = {annual_rate:.3f}%")
    
    # Payback period in years
    print(f"Payback period (user input) = {years} Years")
    
    # Monthly mortgage payment, formatted to two decimal places
    print(f"Monthly payment (output) = ${mortgageMontlyPayment:.2f}")  
    
    # Total payment over the full term, formatted to two decimal places
    print(f"Total payment : ${t:.2f}")


# Call the function to execute the mortgage calculation
calculate_mortgage()

