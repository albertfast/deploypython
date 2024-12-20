# ================================UMPIRE========================================
# Understand:
# Purpose:
# To understand and practice for loops in Python.
#
# Problem Statement:
# In mathematics, the factorial of an integer n, denoted by n! is the following product:
#
# n! = 1 × 2 × … × n
#
# For the given integer n calculate the value n!.
# Input = number, n
# Output = n!
# Restriction : Don't use the math module in this exercise.
# i = 1 => 1 => 1       = i        = 1
# i = 2 => 1*2 => 1!*2 = (i -1)!*i = 2
# i = 3 => 1*2*3 => 2!*3 = (i -1)!*i = 6
# i = 4 => 1*2*3*4 = 3!*4 = (i -1)!*i = 24
#-----------------------------------------
# i = n => 1*2*3..........*n => (n-1)*n = (i -1)!*i
# Match: Sum of N cubes
#
# Plan:
# 1. Input number
# 2. Init factorial
# 3. for all numbers up to number
#    3.1 update factorial, (i -1)!*i
# 4. print factorial

# Implementation:
number = int(input())
factorial = 1
for numbers in range(1,number+1):
    factorial = factorial * numbers
print(factorial)

























