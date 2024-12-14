# Understand:
# Given a list of positive integers called integers, print a row with len(integers)+1 entries as follows:
# first and the last number printed will be 1
# The ith number will be the sum of the value of the (ith-1) and ith numbers in the list integers output a list

# Example      Input:                 Output:
#              1 3 3 1                1 4 6 4 1
#              1 5 10 5 1             1 6 15 15 6 1
#              1 2 3 4 5 6 5 4 3 2 1  1 3 5 7 9 11 11 9 7 5 3 1

##INTERLEAVE false
# def pascalTriangle(lst):
#     result = []
#     for i in range(len(lst)):
#         if i < len(lst) - 1:  # Son elemandan önceki elemanlar için işlem yap
#             result.append(lst[i] + lst[i + 1])  # i ve i+1 elemanlarını topla
#     result.insert(0, 1)  # Listenin başına 1 ekle
#     result.append(1)  # Listenin sonuna 1 ekle
#     return result

def single_number_in_sorted_input(nums):
    for i in range(0, len(nums)-1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[1]
nums = [-2,  -2, 1, 4, 4]
print(single_number_in_sorted_input(nums))
