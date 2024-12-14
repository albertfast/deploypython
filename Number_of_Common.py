# Understand:
# Given two lists of numbers, count how many numbers of the first one occur in the second one.
# Example:    Input:               Output:
#             1 3 2
#             4 3 2                2
#
#             1 7 3 8 10 2 5
#             6 5 2 8 4 3 7        5

# Step 1: Read the two lists of numbers from the user
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

# Step 2: Convert both lists to sets for efficient operations
set1 = set(first_list)
set2 = set(second_list)

# Step 3: Find the intersection of the two sets
common_elements = set1 & set2  # '&' operator gives common elements

# Step 4: Count the number of common elements
count = len(common_elements)

# Step 5: Output the result
print(count)