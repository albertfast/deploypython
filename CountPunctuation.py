# ================================UMPIRE========================================
# Understand:
# Problem: Given a string input, count the number of punctuation marks.
#          For this problem, anything not a letter, number, or whitespace
#          can be considered a punctuation mark.
# Example:
#     Input:  "The quick, brown fox jumps over the lazy dog."
#     Output: 2
#     Input:  "Hands shaking, eyesight fading..."
#     Output: 4
#     Input:  "That'll be $9.95, tip included"
#     Output: 4
#
# Clarifications:
# - Punctuation marks include any symbols from string.punctuation, such as !, ?, ., etc.
# - Only punctuation marks should be counted, ignoring letters, numbers, and spaces.

# Match:
# We can use Python’s string.punctuation constant, which contains all punctuation characters.
# We can iterate through each character in the input string and check if it belongs to string.punctuation.
# If it does, we increment the punctuation count.
# Using a while loop to go through each character and a conditional to check if it is a punctuation mark.

# Plan:
# 1. Import the string module to access string.punctuation, which has all punctuation symbols.
# 2. Initialize a variable punctuation_count to keep track of the number of punctuation marks.
# 3. Use a while loop to iterate through each character of the user input.
# 4. For each character, check if it exists in string.punctuation:
#    - If it does, increment punctuation_count by 1.
# 5. Continue until all characters have been processed.
# 6. Print the final value of punctuation_count.

# Implementation:
import string  # Importing string module to use string.punctuation

# Taking user input as a string
user_input = input("Enter a string: ")

# Initializing a counter for punctuation marks
punctuation_count = 0

# Initializing the index for while loop
index = 0

# Using while loop to iterate through each character in the input string
while index < len(user_input):
    # Checking if the character is in string.punctuation
    if user_input[index] in string.punctuation:
        # Incrementing the punctuation counter
        punctuation_count += 1
    # Moving to the next character
    index += 1

# Printing the total count of punctuation marks
print("Number of punctuation marks:", punctuation_count)
