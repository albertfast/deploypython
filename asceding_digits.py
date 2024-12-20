# ===================== UMPIRE Framework ====================

# Understand:
# Problem Statement: Given a three-digit integer X, determine if its three digits are in ascending order from left to right.
# If so, print "YES"; otherwise, print "NO".
# Example input/output:
# Input: 127 --> Output: YES
# Input: 254 --> Output: NO

# Input: A three-digit integer (X).
# Output: "YES" if the digits are unique and in ascending order, otherwise "NO".
# Restrictions: The input must be a three-digit number with three different digits.

# Match:
# Use basic conditional checks for uniqueness and order of digits.
# Extract individual digits using integer division and modulus operations.

# Plan:
# 1. Verify that the input number is a three-digit integer.
# 2. Extract the hundreds, tens, and units digits from the number.
# 3. Check if all digits are unique and in ascending order.
# 4. Print "YES" if conditions are met; otherwise, print "NO".

# Implementation:
digit_three = int(input())

# Ensure it is a three-digit integer with unique and ascending digits
if 100 <= digit_three <= 999:  # Check if it’s a three-digit number
    hundreds, tens, units = digit_three // 100, (digit_three // 10) % 10, digit_three % 10

    # Check uniqueness and ascending order
    if hundreds < tens < units:
        print("YES")
    else:
        print("NO")
else:
    print("NO")  # If not a three-digit integer

'''
digit_three = int(input())

#Convert the number to a string
digit_three_str = str(digit_three)
digit_three_list = [int(d) for d in digit_three_str]

# Create a set to store digits
digits = set(digit_three_list)

# Initialize a flag to determine uniqueness
unique_digits = len(digit_three_list) == len(digits)
is_in_order = digit_three_list == sorted(digit_three_list)

if unique_digits and is_in_order and len(str(digit_three)) == 3:
    print("YES")
else:
    print("NO")

# Input a three-digit integer
digit_three = int(input())
'''

