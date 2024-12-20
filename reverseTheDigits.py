# ================================UMPIRE========================================
# Understand:
# Input: Take user input integer
# Output: Reverse the integer input by the user
# Restriction : Take user input greater than 9
# Example : Input : 1234 Output: 4321

# Plan:
# 1. Take user input and store it as an integer variable n.
# 2. Initialize an empty list digits to store each digit of n.
# 3. Use a while loop to extract each digit from n and add it to the digits list:
#     - Find the last digit of n using n % 10.
#     - Append this digit to digits.
#     - Remove the last digit from n by integer division (n = n // 10).
# 4. Once all digits are stored in the list, reverse the list order.
# 5. Join the reversed digits into a single number and convert it back to an integer.
# 6. Print the final reversed number.

# Take user input
n = int(input("Enter the number (greater than 9): "))

# Initialize an empty list to store each digit
digits = []
while n > 0:
    # Get the last digit of the number
    remainder = n % 10
    # Append the last digit to the list
    digits.append(remainder)
    # Remove the last digit from the number
    n = n // 10

# Create the reversed number by joining the digits in reverse order
reversed_number = int("".join(map(str, digits)))
print("Final Reversed number:", reversed_number)


#Second Way ==>
#n = int(input("Enter the number (greater than 9): "))
#reverse_number = 0

# Check if the number is greater than 9
#if n > 9:
    #while n > 0:
        #remainder = n % 10  # Get the last digit
        #reverse_number = (reverse_number * 10) + remainder  # Append last digit to the reversed number
        #n = n // 10  # Remove the last digit from n

    #print("Reversed number:", reverse_number)
#else:
    #print("Please enter a number greater than 9.")
