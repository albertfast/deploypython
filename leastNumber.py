# ===================== UMPIRE ====================

# Understand:
# Problem Statement:
# - We need to take 5 integer inputs from the user.
# - Out of these 5 numbers, we must identify and print the smallest number.
#
# Inputs:
# - Five integers provided by the user.
#
# Output:
# - The smallest of the five inputted integers.

# Match:
# - We can use a list to store the five input numbers.
# - Use a for loop to gather input five times and append each input to the list.
# - Initialize the first number as the smallest, then compare each remaining number
#   with this smallest number using conditional statements (if-statements).

# Plan:
# 1. Create an empty list to store the numbers.
# 2. Use a for loop to take 5 integer inputs from the user, appending each to the list.
# 3. Set the first number as the initial smallest number.
# 4. Compare each of the subsequent numbers with the current smallest number and update it if a smaller number is found.
# 5. Print the smallest number.

# Implementation:

numbers = []  # Create an empty list to store the numbers

# Use a for loop to take input 5 times
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)  # Add each input number to the list

# Assume the first number in the list is the smallest initially
smallest_number = numbers[0]

# Compare each of the remaining numbers with the current smallest_number
if numbers[1] < smallest_number:
    smallest_number = numbers[1]
if numbers[2] < smallest_number:
    smallest_number = numbers[2]
if numbers[3] < smallest_number:
    smallest_number = numbers[3]
if numbers[4] < smallest_number:
    smallest_number = numbers[4]

# Print the smallest number
print("The smallest number is:", smallest_number)
print("Use min ",min(numbers))
print("Use Sorted ",sorted(numbers)[0])

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print("The smallest number is:", smallest_number)

# Purpose: Practice input collection and find the minimum number
# Short way
# Create an empty list to store the numbers
numbers = []

# Use a for loop to take input 5 times
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)  # Add the input number to the list

# Find the minimum number in the list
smallest_number = min(numbers)

# Print the smallest number
print("The smallest number is:", smallest_number)

