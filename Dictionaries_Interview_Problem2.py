# Understand:
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_double(lst):
    # Understand:
    # - We need to find if any number in the list appears more than once.
    # - Use a dictionary to track occurrences efficiently.

    # Initialize an empty set to track seen numbers.
    seen = set()

    # Iterate through each number in the list.
    for num in lst:
        # Check if the number is already in the set.
        if num in seen:
            # If found, return True because it's a duplicate.
            return True
        # Otherwise, add the number to the set.
        seen.add(num)

    # If the loop completes without finding duplicates, return False.
    return False

# Examples to Test
# Input: [1, 2, 3, 1]
# Expected Output: True
print(contains_double([1, 2, 3, 1]))

# Input: [1, 2, 3, 4]
# Expected Output: False
print(contains_double([1, 2, 3, 4]))

# Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Expected Output: True
print(contains_double([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
