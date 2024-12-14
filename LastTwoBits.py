# ================================UMPIRE========================================
# Understand:
# Given an integer greater than 9, print its last two bits with space in between.

number = int(input())
number_bin = bin(number)
lst_number_bin = number_bin.split()
print(' '.join(number_bin[-2:]))
print(number_bin)

