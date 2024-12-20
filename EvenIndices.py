# Understand
# Given a list of numbers, find and print all its elements with even indices (i.e. A[0], A[2], A[4], ...).
# Example                  Input:            Output:
#
#                           5 6 7 8 9         5 7 9
#                           4 5 3 4 2 3       4 3 2
#                           6                 6
#    40 64 -80 -98 -68 56 85 87 -68 -78       40 -80 -68 85 -68

# Implementation:

# Read input from the user, split it into a list, and convert each item to an integer.
a_list = [int(str_numbers) for str_numbers in input().split()]

def even_indices(a_list):
    odd_index = [(a_list[i]) for i in range(len(a_list)) if i % 2 == 0 and (len(a_list) >= 2)]
    if odd_index:
        print(*odd_index)
    else:
        print(a_list[0])
# Call the function with the list as an argument
even_indices(a_list)

for index, value in enumerate(a_list):
    if index % 2 == 0:
        print(f"Index {index}: {value}")
'''
def even_indices(a_list):
    # If the list has only one element, print that element
    if len(a_list) == 1:
        print(a_list[0])
    else:
        # Otherwise, iterate through indices of the list
        for i in range(len(a_list)):
            # Check if the index is even
            if i % 2 == 0:
                # Print the element at this even index
                print(a_list[i], end=' ')
# Call the function with the list as an argument
even_indices(a_list)
'''














