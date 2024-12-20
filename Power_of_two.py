# ================================UMPIRE========================================
# Understand:
#
# Purpose:
# To understand and practice while loops in Python.
#
# Problem Statement:
# For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X.
# Print the exponent value and the result of the expression 2ⁿ.
# Example: Input: 50 Output: 5 32 || 2ⁿ = 2 ** 5 = 32 it is okay because 50 > 32 until 2 ** 6 = 64 because 50 < 64

input_number = int(input())

n = 0

while  input_number >= 2 ** n:
    n += 1
n -=1  # Decrement n by 1 because the loop increments it one step further
print(n, 2 ** n)

# 2nd way
# Find the greatest exponent n where 2^n is less than or equal to input_number
n = input_number.bit_length() - 1

# Calculate 2^n
result = 2 ** n

print("n =", n, "2ⁿ =", result)





















