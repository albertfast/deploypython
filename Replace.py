# ================================UMPIRE========================================
# Understand:
# Given a string. Replace in this string all the numbers 1 by the word one.
#
# Input: A string that may or may not contain the digit 1.
# Output: A new string where every 1 is replaced by "one" while other characters remain unchanged.
#
# Examples:
# Input: "1+1=2"
# Output: "one+one=2"
#
# Input: "Hello, 2345678990"
# Output: "Hello, 2345678990" (No changes as 1 is not present)
#
# Input: "1"
# Output: "one"
#
# Input: "1111111111"
# Output: "oneoneoneoneoneoneoneoneoneone"
#
# Input: "1213141516171819101"
# Output: "one2one3one4one5one6one7one8one9one0one"

# Match:
# - The replacement logic resembles string manipulation or traversal.
# - We can iterate through the string character by character using a loop:
#   - If the current character is '1', append "one" to the result.
#   - Otherwise, append the original character.
# - Python's string concatenation or list-based construction can be used.
# - We use a for or while loop to traverse the string.

# Plan:
# Step 1: Take input from the user as a string.
# Step 2: Initialize an empty string to hold the modified version of the input.
# Step 3: Loop through the string:
#         - If the character is '1', append "one" to the result string.
#         - Otherwise, append the original character.
# Step 4: Print the resulting string.

# Implementation:
#
# Step 1: Take input from the user
input_string = input("Enter a string: ")

# Step 2: Initialize an empty string to hold the result
result = ""

# Step 3: Traverse each character in the input string
for char in input_string:
    if char == '1':  # If the character is '1', replace it with "one"
        result += "one"
    else:  # Otherwise, keep the original character
        result += char

# Step 4: Print the resulting string
print(result)

#Second Solution
# Take input from user
input_string = input("Enter a string: ")

# Initialize variables
result = ""
index = 0

# Traverse the string with a while loop
while index < len(input_string):
    if input_string[index] == '1':  # Replace '1' with "one"
        result += "one"
    else:  # Keep other characters as they are
        result += input_string[index]
    index += 1

# Print the result
print(result)
