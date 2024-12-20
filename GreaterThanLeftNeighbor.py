# Understand:
# Given a list of numbers, create a new list with its elements that are greater
# than their left neighbor and print the content of this new list.

a_list = [int(str_number) for str_number in input().split()]

def greater_than_left_neighbor(a_list):
   # new_list = [value for index, value in enumerate(a_list[1:], start=1) if value > a_list[index - 1]]   ==> List comprehension
    for index, value in enumerate(a_list):
        if index == 0:
            continue
        elif value > a_list[index - 1]:
            print(value, end=' ')
    return
greater_than_left_neighbor(a_list)