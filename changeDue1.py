# Get user input for cash payment and amount tendered
# The program prompts the user to enter two amounts:
# - The cash payment (the cost of the item or service).
# - The amount tendered (the money given by the customer to cover the payment).
# Both inputs are accepted as integers (whole numbers) representing dollar amounts.
cashPayment = int(input("Enter the cash payment amount: "))
amountTendered = int(input("Enter the amount tendered: "))

# Check if the cash payment is valid (not zero or negative and less than or equal to the amount tendered)
# Before proceeding with any calculations, the program ensures the following:
# - The cash payment is a positive value (greater than zero).
# - The amount tendered is not less than the cash payment.
# If either condition is violated, the program displays an error message and stops.
if cashPayment <= 0:
    # If the cash payment is zero or negative, print an error message
    print("Error: The cash payment must be greater than zero.")
elif cashPayment > amountTendered:
    # If the cash payment is greater than the amount tendered, print an error message
    print("Error: The cash payment cannot be greater than the amount tendered.")
else:
    # Calculate the change due by subtracting cash payment from the amount tendered
    # Once the inputs are validated, the program calculates the change by subtracting the cash payment from the amount tendered.
    changeDue = amountTendered - cashPayment

    # Print the payment details: cash payment, amount tendered, and change due
    # The program outputs the values for the cash payment, the amount tendered, and the total change due.
    print("Cash payment amount: ", cashPayment)
    print("Tendered amount: ", amountTendered)
    print("Change due: ", changeDue)
    print("\nChange paid out in:\n ")
    
    # The following section breaks down the total change into the fewest number of bills.
    # The program starts with the largest denomination ($100,000) and works its way down to $1 bills.
    # It uses integer division ('//') to determine how many bills of a certain denomination are needed
    # and the modulo operator ('%') to calculate the remaining amount after accounting for those bills.
    
    # Calculate how many $100,000 bills are in the change due
    hundredThousands = changeDue // 100000  # Integer division to determine how many $100,000 bills can be used
    changeDue = changeDue % 100000  # The remaining amount after using $100,000 bills
    print("This many hundred thousand dollar bills: ", hundredThousands)

    # Repeat the same process for smaller denominations down to $1 bills.
    tenThousands = changeDue // 10000
    changeDue = changeDue % 10000
    print("This many ten thousand dollar bills: ", tenThousands)

    fiveThousands = changeDue // 5000
    changeDue = changeDue % 5000
    print("This many five thousand dollar bills: ", fiveThousands)

    thousands = changeDue // 1000
    changeDue = changeDue % 1000
    print("This many thousand dollar bills: ", thousands)

    fiveHundreds = changeDue // 500
    changeDue = changeDue % 500
    print("This many five hundred dollar bills: ", fiveHundreds)

    hundreds = changeDue // 100
    changeDue = changeDue % 100
    print("This many hundred dollar bills: ", hundreds)

    fifties = changeDue // 50
    changeDue = changeDue % 50
    print("This many fifty dollar bills: ", fifties)

    twenties = changeDue // 20
    changeDue = changeDue % 20
    print("This many twenty dollar bills: ", twenties)

    tens = changeDue // 10
    changeDue = changeDue % 10
    print("This many ten dollar bills: ", tens)

    fives = changeDue // 5
    changeDue = changeDue % 5
    print("This many five dollar bills: ", fives)

    twos = changeDue // 2
    changeDue = changeDue % 2
    print("This many two dollar bills: ", twos)

    # Finally, calculate how many $1 bills are in the remaining change
    ones = changeDue // 1
    print("This many one dollar bills: ", ones)
