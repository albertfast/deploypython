# ================================UMPIRE========================================
# Understand:
# Purpose:
# Given a sequence of non-negative integers where each number is written (input) on a separate line,
# determine the length of the sequence.
# The sequence ends when a 0 is entered, and we do not count the 0 as part of the sequence.
# Any numbers after 0 should be ignored.
#
# Input:
# The input consists of multiple integers written one after another.
#
# Output:
# Print the length of the sequence excluding 0.
#
# Example:
# Input: 1, 7, 9, 0, 5
# Output: 3 (Only the numbers 1, 7, and 9 are counted)

# Match:
# - We need to use a while loop since we do not know how many inputs will be provided.
# - Use a counter (sequence_count) to count numbers before a 0.
# - The loop terminates when 0 is entered.
#
# Plan:
# 1. Initialize a counter sequence_count to 0.
# 2. Start a while loop to take user input until the input is 0.
#    - Increment the counter for each valid (non-zero) input.
#    - Break the loop when the input is 0.
# 3. After the loop ends, print the sequence_count.

# Implementation:
# Step 1: Initialize variables
input_number = int(input())  # First input
sequence_count = 0  # Counter for the sequence length

# Step 2: Use a while loop to process the input
while input_number != 0:  # Continue until a 0 is entered
    sequence_count += 1   # Increment the counter for each valid number
    input_number = int(input())  # Take the next input

# Step 3: Print the result after the loop ends
print(sequence_count)  # Output the sequence length
