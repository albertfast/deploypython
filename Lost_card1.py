# Purpose:
# To understand and practice for loops and arithmetic operations in Python.

# Problem Statement:
# There was a set of cards with numbers from 1 to N. One of the cards is now lost. Determine the number on that lost card given the numbers for the remaining cards.

# Input: Total number of cards (N)
number = int(input("Enter the total number of cards: "))

# Calculate the sum of all numbers from 1 to N using the formula
expected_sum = number * (number + 1) // 2  # Formula: N * (N + 1) / 2
print(f"Expected sum of all cards (1 to {number}): {expected_sum}")

# Initialize actual_sum to calculate the sum of given numbers
actual_sum = 0
print("Starting to collect the numbers of the remaining cards...\n")

# Loop through the remaining N-1 numbers
for i in range(1, number):  # Loop runs (N-1) times
    card = int(input(f"Enter card number {i}: "))
    actual_sum += card
    # Print details at each iteration
    print(f"Iteration {i}: Added card {card}. Current total of remaining cards: {actual_sum}")

# The missing number is the difference between expected_sum and actual_sum
missing_number = expected_sum - actual_sum

# Output the missing number
print("\nAll cards processed.")
print(f"The missing card number is: {missing_number}")
