# ================================UMPIRE========================================
# Understand :
# In bowling, the player starts with 10 pins in a row at the far end of a lane. The goal is to knock all the pins down.
# For this assignment, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled,
# followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled.
#
# The balls are numbered from 1 to N for this situation. The subsequent number pairs, one for each K represent the first and last (inclusive)
# positions of the pins that were knocked down with each roll. Print a sequence of N characters, where "I" represents a pin left standing and "."
# represents a pin knocked down.

# Input:
# - N: Number of pins in a row.
# - K: Number of rolls (or attempts).
# - For each roll, two numbers (first and last) represent the range of pins knocked down.
# Output:
# - A string of length N:
#   - "I" represents a pin still standing.
#   - "." represents a pin knocked down.

# Example:
# Input:
# 10 3
# 1 3
# 2 5
# 3 6
# Output:
# I.....I...

# Restrictions:
# 1. N and K are positive integers.
# 2. Pins are numbered from 1 to N.
# 3. The ranges (first to last) are inclusive and valid within the bounds of N.

# Match:
# 1. Use a list to represent pins ("I" for standing, "." for knocked down).
# 2. For each roll, update the corresponding range in the list to ".".
# 3. After processing all rolls, convert the list to a string and print the result.

# Plan:
# 1. Initialize a list of "I" with length N to represent all pins standing.
# 2. For each roll (K rolls total):
#    a. Read the range (first to last).
#    b. Update the list from index first - 1 to last - 1 to ".".
# 3. After all rolls, print the list as a string.

# Implementation:

##INTERLEAVE false
##INTERLEAVE false
def update_bowling_configuration(pins, first, last):
    '''Updates the pins configuration by marking the pins from "first" to "last" as knocked down (".")'''
    # Update the range of pins from first-1 to last-1 to "."
    for i in range(first - 1, last):
        pins[i] = '.'  # Mark the pin as knocked down

# Main program
try:
    n, k = [int(str_numbers) for str_numbers in input("Enter number of pins and rolls (N K): ").split()]
    if n <= 0 or k <= 0:
        raise ValueError("N and K must be positive integers.")
    pins = ['I'] * n  # All pins start as standing ("I")

    # Process each roll
    for rolls in range(k):
        while True:
            try:
                # Input for each roll
                first, last = [int(s) for s in input(f"Enter range for roll {rolls + 1} (first last): ").split()]
                # Validate range
                if first < 1 or last > n or first > last:
                    print(f"Invalid range! Pins must be between 1 and {n}, and first <= last.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid input! Please enter two integers separated by a space.")
        update_bowling_configuration(pins, first, last)

    # Print the final state of the pins
    print(''.join(pins))  # Convert the list to a string and print
except ValueError as e:
    print(f"Error: {e}")
