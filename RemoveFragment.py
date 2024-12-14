# ================================UMPIRE========================================
# Understand:
# Problem Statement:
# Given a string in which the letter 'h' occurs at least twice, remove from that string the first 
# and the last occurrence of the letter 'h', as well as all the characters between them.

# Examples:
# Input: "In the hole in the ground there lived a hobbit"
# Output: "In tobbit"
# Explanation: The first 'h' is removed along with the last 'h' and everything in between.

# Input: "qwertyhasdfghzxcvb"
# Output: "qwertyzxcvb"
# Explanation: The first 'h' and the last 'h', along with the characters in between, are removed.

# Input: "ahahahahaha"
# Output: "aa"
# Explanation: The first 'h' and the last 'h', along with everything in between, are removed.

# Match:
# - The logic is similar to problems where we identify the first and last occurrence of a character,
#   such as finding the first and last occurrence of 'p' or removing a fragment based on these indices.
# - Here, we use str.find() to locate the first occurrence of 'h' and str.rfind() to locate the last occurrence.
# - Then, we use string slicing to exclude the specified fragment from the string.

# Plan:
# 1. Take the input string from the user.
# 2. Find the index of the first occurrence of 'h' using str.find().
#     - If 'h' does not occur at least twice, output the original string.
# 3. Find the index of the last occurrence of 'h' using str.rfind().
# 4. Use string slicing to construct a new string that excludes the portion from the first 'h' to the last 'h'.
# 5. Print the resulting string.

# Implementation:
str_input = input("Enter the string: ")  # Step 1: Take user input

# Step 2: Find the first occurrence of 'h'
first_h_index = str_input.find('h')

# Step 3: Find the last occurrence of 'h'
last_h_index = str_input.rfind('h')

if first_h_index == -1 or first_h_index == last_h_index:
    # If 'h' does not occur at least twice, return the original string
    print(str_input)
else:
    # Step 4: Remove the fragment between the first and last 'h'
    result = str_input[:first_h_index] + str_input[last_h_index + 1:]
    print(result)

# ================================EXPLANATION==================================
# - The program first identifies whether 'h' occurs in the string using str.find() and str.rfind().
# - If 'h' does not occur at least twice, the string remains unchanged.
# - If 'h' occurs at least twice, the program constructs a new string by combining the portion
#   before the first occurrence and after the last occurrence using string slicing.
# - This approach effectively removes the specified fragment, fulfilling the requirements of the problem.

