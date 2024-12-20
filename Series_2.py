# ================================UMPIRE========================================
# Understand:
# Given two integers A and B. Print all numbers from A to B inclusively, in increasing order,
# if A < B, or in decreasing order, if A ≥ B.
# - In **increasing order** if A < B.
# - In **decreasing order** if A ≥ B.

# Input:
# Two integers A and B.

# Output:
# A sequence of numbers from A to B, printed in a single line separated by spaces.

# Examples:
# 1. Input: A = 8, B = 5
#    Output: 8 7 6 5
# 2. Input: A = 1, B = 10
#    Output: 1 2 3 4 5 6 7 8 9 10
# 3. Input: A = 179, B = 179
#    Output: 179

# Match:
# - We need to use a for loop because the problem explicitly asks for a sequence between two values.
# - To determine the direction (increasing or decreasing), we compare A and B:
#   - If A < B, use range(A, B + 1) to count upward inclusively.
#   - If A ≥ B, use range(A, B - 1, -1) to count downward inclusively.

# Plan:
# 1. Take two integer inputs A and B from the user.
# 2. Use a conditional statement to check the relationship between A and B:
#    - If A < B, use a for loop with range(A, B + 1) to print in increasing order.
#    - If A ≥ B, use a for loop with range(A, B - 1, -1) to print in decreasing order.
# 3. Print the numbers in a single line, separated by spaces.

# Implementation:
# Step 1: Take inputs for A and B
A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))

# Step 2: Determine the order and print the sequence
if A < B:
    for number in range(A, B + 1):  # Increasing order
        print(number, end=" ")
else:
    for number in range(A, B - 1, -1):  # Decreasing order
        print(number, end=" ")