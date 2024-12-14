# Understand:
# Given a list of numbers, print all its even elements.
# Use a for-loop that iterates over the list itself and not over its indices. That is, don't use range().

a_list = [int(str_numbers) for str_numbers in input().split()]
def even_elements(a_list):
    for i in range(len(a_list)):
        if a_list[i] % 2 == 0:
            print(a_list[i], end=' ')
    return
even_elements(a_list)

'''
# Iterate over elements directly, not their indices
for number in a_list:
    # Check if the element is even
    if number % 2 == 0:
        # Print the even elements separated by space, without new line
        print(number, end=' ')
'''