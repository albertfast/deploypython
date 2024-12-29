# Get user input for cash payment and amount tendered
cashPayment = int(input("Enter the cash payment amount: "))
amountTendered = int(input("Enter the amount tendered: "))

# Check if the cash payment is valid (not zero or negative and less than or equal to the amount tendered)
if cashPayment <= 0:
    # If cash payment is zero or negative, print an error message
    print("Error: The cash payment must be greater than zero.")
elif cashPayment > amountTendered:
    # If cash payment is greater than the amount tendered, print an error message
    print("Error: The cash payment cannot be greater than the amount tendered.")
else:
    # Calculate the change due by subtracting cash payment from the amount tendered
    changeDue = amountTendered - cashPayment

    # Print the payment details: cash payment, amount tendered, and change due
    print("Cash payment amount: ", cashPayment)
    print("Tendered amount: ", amountTendered)
    print("Change due: ", changeDue)
    print("Change paid out in: ")

    # Calculate how many $100,000 bills are in the change due
    hundredThousands = changeDue // 100000
    # Update the remaining change after accounting for $100,000 bills
    changeDue = changeDue % 100000
    # Print the number of $100,000 bills
    print("This many hundred thousand dollar bills: ", hundredThousands)

    # Calculate how many $10,000 bills are in the remaining change
    tenThousands = changeDue // 10000
    # Update the remaining change after accounting for $10,000 bills
    changeDue = changeDue % 10000
    # Print the number of $10,000 bills
    print("This many ten thousand dollar bills: ", tenThousands)

    # Calculate how many $5,000 bills are in the remaining change
    fiveThousands = changeDue // 5000
    # Update the remaining change after accounting for $5,000 bills
    changeDue = changeDue % 5000
    # Print the number of $5,000 bills
    print("This many five thousand dollar bills: ", fiveThousands)

    # Calculate how many $1,000 bills are in the remaining change
    thousands = changeDue // 1000
    # Update the remaining change after accounting for $1,000 bills
    changeDue = changeDue % 1000
    # Print the number of $1,000 bills
    print("This many thousand dollar bills: ", thousands)

    # Calculate how many $500 bills are in the remaining change
    fiveHundreds = changeDue // 500
    # Update the remaining change after accounting for $500 bills
    changeDue = changeDue % 500
    # Print the number of $500 bills
    print("This many five hundred dollar bills: ", fiveHundreds)

    # Calculate how many $100 bills are in the remaining change
    hundreds = changeDue // 100
    # Update the remaining change after accounting for $100 bills
    changeDue = changeDue % 100
    # Print the number of $100 bills
    print("This many hundred dollar bills: ", hundreds)

    # Calculate how many $50 bills are in the remaining change
    fifties = changeDue // 50
    # Update the remaining change after accounting for $50 bills
    changeDue = changeDue % 50
    # Print the number of $50 bills
    print("This many fifty dollar bills: ", fifties)

    # Calculate how many $20 bills are in the remaining change
    twenties = changeDue // 20
    # Update the remaining change after accounting for $20 bills
    changeDue = changeDue % 20
    # Print the number of $20 bills
    print("This many twenty dollar bills: ", twenties)

    # Calculate how many $10 bills are in the remaining change
    tens = changeDue // 10
    # Update the remaining change after accounting for $10 bills
    changeDue = changeDue % 10
    # Print the number of $10 bills
    print("This many ten dollar bills: ", tens)

    # Calculate how many $5 bills are in the remaining change
    fives = changeDue // 5
    # Update the remaining change after accounting for $5 bills
    changeDue = changeDue % 5
    # Print the number of $5 bills
    print("This many five dollar bills: ", fives)

    # Calculate how many $2 bills are in the remaining change
    twos = changeDue // 2
    # Update the remaining change after accounting for $2 bills
    changeDue = changeDue % 2
    # Print the number of $2 bills
    print("This many two dollar bills: ", twos)

    # Calculate how many $1 bills are in the remaining change
    ones = changeDue // 1
    # Print the number of $1 bills
    print("This many one dollar bills: ", ones)

    
