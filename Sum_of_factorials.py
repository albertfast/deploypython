# In mathematics, the factorial of an integer n, denoted by n! is the following product:
#
# n! = 1 × 2 × … × n
#
# For the given integer n calculate the value
#
# 1! + 2! + 3! + ... + n!
#
# Try to discover the solution that uses only one for-loop. And don't use the math module in this exercise.

number = int(input())
sum = 0
factorial = 1
for numbers in range(1,number+1):
    factorial *= numbers
    sum += factorial
print(sum)
