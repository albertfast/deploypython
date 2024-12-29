# Get user input for cash payment and amount tendered
# The program prompts the user to input the total amount of the transaction (cash payment) and the amount tendered (money given by the customer).
cashPayment = float(input("Enter the cash payment amount (in dollars): "))
amountTendered = float(input("Enter the amount tendered (in dollars): "))

# Check if the cash payment is valid (not zero or negative and less than or equal to the amount tendered)
# The program first validates the inputs to ensure that:
# 1. The payment amount is greater than zero.
# 2. The amount tendered is not less than the cash payment.
# If any condition is violated, the program will display an error message and stop.
if cashPayment <= 0:
    print("Error: The cash payment must be greater than zero.")
elif cashPayment > amountTendered:
    print("Error: The cash payment cannot be greater than the amount tendered.")
else:
    # Calculate the change due by subtracting cash payment from the amount tendered
    # Once the inputs are validated, the program calculates the change to be returned by subtracting the cash payment from the tendered amount.
    changeDue = amountTendered - cashPayment

    # Separate the dollars and cents
    # The total change is then split into two parts: dollars and cents.
    # - `dollars` represents the whole number part (integer division).
    # - `cents` represents the fractional part, multiplied by 100 to avoid floating point errors.
    dollars = int(changeDue)  # The whole dollar part
    cents = round((changeDue - dollars) * 100)  # The cents part, rounded to avoid floating point errors

    # Print the payment details: cash payment, amount tendered, and change due
    print("\nCash payment amount: $", cashPayment)
    print("Tendered amount: $", amountTendered)
    print("Change due: $", changeDue)
    print("\nChange paid out in: ")
    print("")

    # The program now calculates the number of bills needed for each denomination, starting with the largest (100,000 dollars)
    # The '//' operator is used for integer division to find out how many bills of a certain denomination can be used.
    # The '%' operator calculates the remaining amount after accounting for those bills.
    
    # Calculate how many $100,000 bills are in the change due
    # Example: If we have $345,000, 345000 // 100000 gives 3 (three $100,000 bills).
    hundredThousands = dollars // 100000
    dollars = dollars % 100000  # The remainder after accounting for $100,000 bills
    print("This many hundred thousand dollar bills: ", hundredThousands)

    # Repeat the same process for $10,000 bills
    tenThousands = dollars // 10000
    dollars = dollars % 10000
    print("This many ten thousand dollar bills: ", tenThousands)

    # Calculate how many $5,000 bills are in the remaining change
    fiveThousands = dollars // 5000
    dollars = dollars % 5000
    print("This many five thousand dollar bills: ", fiveThousands)

    # Calculate how many $1,000 bills are in the remaining change
    thousands = dollars // 1000
    dollars = dollars % 1000
    print("This many thousand dollar bills: ", thousands)

    # Continue for smaller bills like $500, $100, $50, $20, $10, $5, and $1
    fiveHundreds = dollars // 500
    dollars = dollars % 500
    print("This many five hundred dollar bills: ", fiveHundreds)

    hundreds = dollars // 100
    dollars = dollars % 100
    print("This many hundred dollar bills: ", hundreds)

    fifties = dollars // 50
    dollars = dollars % 50
    print("This many fifty dollar bills: ", fifties)

    twenties = dollars // 20
    dollars = dollars % 20
    print("This many twenty dollar bills: ", twenties)

    tens = dollars // 10
    dollars = dollars % 10
    print("This many ten dollar bills: ", tens)

    fives = dollars // 5
    dollars = dollars % 5
    print("This many five dollar bills: ", fives)

    ones = dollars // 1
    print("This many one dollar bills: ", ones)

    # After calculating the whole dollar amounts, we move on to calculate the coins.
    # Coins are calculated similarly to bills, starting with the largest coin (quarters) and moving to the smallest (pennies).
    
    # Now calculate the coins (quarters, dimes, nickels, pennies) from the cents part
    # Example: For 94 cents, 94 // 25 gives 3 quarters, and the remainder (94 % 25) is used to calculate the smaller coins.
    quarters = cents // 25
    cents = cents % 25
    print("This many quarters: ", quarters)

    dimes = cents // 10
    cents = cents % 10
    print("This many dimes: ", dimes)

    nickels = cents // 5
    cents = cents % 5
    print("This many nickels: ", nickels)

    pennies = cents // 1
    print("This many pennies: ", pennies)

