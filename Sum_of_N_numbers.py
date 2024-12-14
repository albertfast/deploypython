# ================================UMPIRE========================================
# Understand:
# Purpose:
# To understand and practice for loops in Python.
#
# Problem Statement:
# N numbers are given in the input. Read them and print their sum.
#
# The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer.
# Print the sum of these N integers.

# Input : N, numbers to follow
# # Output: print the sum
# # Example: N = 4
# # ask for an integer 4 times:
# # as you enter get the sum
#
# Match: Sum of sequence, Sum of 10 numbers

# Plan:
# 1. Input N
# 2. Init sum
# 3. for N times:
#       3.1 input an integer
#       3.2 add it to the sum
# 4. print the sum

# Implementation:
number = int(input())
sum = 0
for numbers in range(number):
    #sum = sum + int(input())
    sum += int(input())
    #print(numbers, " ", sum)
print(sum)
