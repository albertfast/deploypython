# ================================UMPIRE========================================
# Understand:
# Given a search term and a series of 8 inputs, find the index/position of the search term in the series.
# If the search term is not found, print "NOT FOUND". Note that we start counting from 0
# (the first element is in index 0, the second in index 1, and so on).
# Note: Each number is unique, so don't need to worry about repeating numbers.
# Example:                  Input:                                  Output:
#                           12
#                           12 2 84 38 29 43 68 21                   0
#
#                           5(Search Number)                         4
#                           1
#                           2
#                           3
#                           4
#                           5
#                           6
#                           7
#                           8

#                           5
#                           32 28 53 21 93 10 49 27                NOT FOUND
#                           (Each number is separate input, see above)

# Match:
# We need to search for a term in a list of numbers and return its index if found.
# We can use a list to store the series of numbers, and check if the search term is in the list.
# If present, we can use the .index() method to find its position.
# Alternatively, we can use a while loop to search for the term as we receive each input,
# stopping early if the term is found.

# Plan 1 (Using a List and Final Search Check):
# 1. Take input for the search term.
# 2. Take 8 integer inputs from the user and store them in a list.
# 3. Check if the search term is in the list:
#    - If found, print its index.
#    - If not found, print "NOT FOUND".

# Plan 2 (Using a While Loop for Early Exit):
# 1. Take input for the search term.
# 2. Initialize an index counter and an empty list to store the numbers.
# 3. Use a while loop to take up to 8 inputs:
#    - Add each number to the list.
#    - Check if the current number matches the search term:
#       - If yes, print the index and exit the loop.
#       - If no, continue to the next number.
# 4. After the loop, if the search term was not found, print "NOT FOUND".

# ================================== Plan 1 ==================================

# Implementation of Plan 1
# search_num = int(input("Enter the number to search for: "))  # Step 1: Taking search term

# Step 2: Taking 8 integer inputs and storing them in a list
# numbers = [int(input("Enter a number: ")) for _ in range(8)]

# Step 3: Checking if the search term is in the list
# if search_num in numbers:
   # print(numbers.index(search_num))  # If found, print the index
# else:
#     print("NOT FOUND")  # If not found, print "NOT FOUND"

# Explanation:
# - We take the search term and 8 numbers as input.
# - We check if the search term exists in the list `numbers`.
# - If the term exists, we print its index using the .index() method.
# - If it doesn’t exist, we print "NOT FOUND".
# - This solution requires all 8 inputs to be gathered before checking for the search term.

# ================================== Plan 2 ==================================

# Implementation of Plan 2
search_num = int(input("Enter the number to search for: "))  # Step 1: Taking search term

# Initializing variables
found = False  # A flag to check if the search number has been found
index = 0  # Index counter
numbers = []  # List to store numbers for reference (optional but useful)

# Step 3: Using a while loop to take up to 8 inputs or exit early if found
while index < 8:
    num = int(input("Enter a number: "))
    numbers.append(num)  # Adding each number to the list (for reference)

    if num == search_num:
        found = True
        print(index)  # Printing the index where search term was found
        break  # Exiting the loop as the search term is found

    index += 1  # Incrementing the index counter

# Step 4: After loop, if the search term is not found, print "NOT FOUND"
if not found:
    print("NOT FOUND")

# Explanation:
# - We start by taking the search term from the user.
# - We use a `while` loop to accept up to 8 inputs, appending each to `numbers` for reference.
# - If we encounter the search term during input, we print the current `index` and exit the loop.
# - If we reach the end of the loop without finding the search term, we print "NOT FOUND".
# - This solution is more efficient because it exits early if the search term is found, avoiding unnecessary inputs.

# ================================== Summary ==================================
# - Plan 1 is straightforward and gathers all 8 inputs before checking for the search term.
# - Plan 2 is more efficient by using a `while` loop, allowing for early exit if the search term is found.
# - Plan 2 is generally preferred for its efficiency, as it doesn’t require all 8 inputs if the search term appears early.
