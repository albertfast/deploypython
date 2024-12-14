# ================================UMPIRE========================================
# Understand:
# Given an integer n that is greater than or equal to 2, find its smallest integer divisor greater than 1.
# In other words, find the smallest number d (where d > 1) such that n % d == 0.
#
# Example:
# Input: n = 15
# Output: 3 (3 is the smallest integer greater than 1 that divides 15 without a remainder)
#
# Input: n = 7
# Output: 7 (7 is a prime number, so its smallest divisor greater than 1 is itself)
#
# Input: n = 12
# Output: 2 (2 is the smallest integer greater than 1 that divides 12 without a remainder)
#
# The problem tests the ability to use loops and modulus operations to find divisors.

# Match:
# We need to find the smallest divisor of n greater than 1.
# A suitable approach is:
# 1. Start with the smallest possible divisor, which is 2.
# 2. Check if n is divisible by 2, 3, 4, etc., until a divisor is found.
# 3. Use a while loop to incrementally test each divisor until one that divides n without a remainder is found.
# 
# Using the modulus operation (n % divisor == 0), we can check divisibility.

# Plan:
# 1. Initialize divisor to 2, the smallest integer greater than 1.
# 2. Use a while loop to keep checking divisors:
#    - While n is not divisible by divisor, increment divisor by 1.
# 3. When a divisor is found (i.e., n % divisor == 0), the loop stops, and we print the divisor.

# Implementation:
n = int(input("Enter a number greater than 1: "))  # Step 1: Take the integer input n
divisor = 2                                       # Step 2: Start with the smallest divisor, 2

# Step 3: Loop until a divisor is found
while n % divisor != 0:
    divisor += 1  # Increment divisor by 1 if divisor does not divide n evenly

# Step 4: Print the smallest divisor found
print(divisor)

# Explanation:
# - We start by initializing divisor to 2.
# - The while loop checks if divisor divides n without a remainder (n % divisor == 0).
# - If the remainder is not zero, we increase divisor by 1 and check again.
# - The loop stops as soon as we find the smallest divisor of n greater than 1.

# Example Walkthrough:
# For n = 15:
#   - divisor = 2: 15 % 2 != 0, so we increment divisor.
#   - divisor = 3: 15 % 3 == 0, so we stop and print 3.
#
# For n = 7 (a prime number):
#   - divisor = 2: 7 % 2 != 0, so we increment divisor.
#   - divisor = 3: 7 % 3 != 0, so we increment divisor.
#   - divisor = 4: 7 % 4 != 0, so we increment divisor.
#   - ...
#   - Finally, when divisor = 7, 7 % 7 == 0, so we print 7.

# Review:
# - The solution efficiently finds the smallest divisor greater than 1 by incrementally checking divisors.
# - The use of the modulus operation ensures we correctly identify divisors without needing complex calculations.

# Evaluate:
# - This solution is efficient and works well within the constraints, especially since n >= 2.
# - For prime numbers, it correctly identifies that the smallest divisor greater than 1 is the number itself.
