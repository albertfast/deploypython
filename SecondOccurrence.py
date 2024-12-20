# ================================UMPIRE========================================
# Understand:
# Given a string that may contain a letter p. Print the index of the second occurrence of p.
# If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.
# Examples:              Input:                      Output:
#                        apple                         2 (The second occurrence of 'p' is at index 2)
#                        grape                        -1 (The letter 'p' occurs only once)
#                        banana                       -2 (The string does not contain 'p')

# Match:
# - The logic for identifying occurrences is similar to the first and last occurrence of a character.
# - In the previous problem, we used str.find() for the first occurrence and str.rfind() for the last occurrence.
# - Here, we extend the usage of str.find() by specifying the starting position after the first occurrence.

# Plan:
# 1. Take the input string from the user.
# 2. Use str.find('p') to find the index of the first occurrence of 'p'.
#     - If the result is -1, the string does not contain 'p', so print -2.
# 3. If the first occurrence is found:
#     - Use str.find('p', first_occurrence + 1) to find the index of the second occurrence.
#     - If the result is -1, print -1 (indicating only one occurrence of 'p').
# 4. Otherwise, print the index of the second occurrence.

# Implementation:


str_input = input("Enter the string: ")  # Step 1: Take user input

# Step 2: Find the first occurrence of 'p'
first_occurrence = str_input.find('p')

if first_occurrence == -1:
    # If 'p' is not found at all, print -2
    print(-2)
else:
    # Step 3: Find the second occurrence of 'p'
    second_occurrence = str_input.find('p', first_occurrence + 1)
    if second_occurrence == -1:
        # If only one 'p' is found, print -1
        print(-1)
    else:
        # Otherwise, print the index of the second occurrence
        print(second_occurrence)
