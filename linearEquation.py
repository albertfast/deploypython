# ===================== UMPIRE ====================

# Understand:
# Problem Statement:
# - We are given an equation in the form of ax = b.
# - We need to determine if there is an integer solution for x.
# - If there is a unique integer solution, we should print that solution.
# - If there is no solution, print "no solution".
# - If there are infinitely many solutions, print "many solutions".

# Inputs:
# - Two integers, 'a' and 'b', representing the coefficients of the equation ax = b.

# Output:
# - If there is a unique integer solution for x, print that integer.
# - If there are no solutions, print "no solution".
# - If there are infinitely many solutions, print "many solutions".

# Restrictions:
# - Only integers are considered as input values for 'a' and 'b'.
# - Use basic mathematical operations and if-else conditions to evaluate the solution.

# Match:
# - We will use conditional statements to evaluate different cases:
#   1. If a = 0 and b = 0, then there are infinitely many solutions ("many solutions").
#   2. If a = 0 and b != 0, or if b is not divisible by a, then there is no solution.
#   3. If a != 0 and b is divisible by a, then there is a unique integer solution x = b / a.

# Plan:
# 1. Take input for 'a' and 'b'.
# 2. Check if both 'a' and 'b' are zero. If true, print "many solutions".
# 3. If 'a' is zero and 'b' is non-zero, or if 'b' is not divisible by 'a', print "no solution".
# 4. If 'a' is non-zero and 'b' is divisible by 'a', print the integer solution x = b // a.

# Implementation:
# Step 1: Take user input for 'a' and 'b'
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Step 2: Determine the type of solution based on the value of 'a' and 'b'
if a == 0 and b == 0:
    # Case where both 'a' and 'b' are zero, leading to infinite solutions
    print("many solutions")
elif a == 0 and b != 0 or b % a != 0:
    # Case where 'a' is zero and 'b' is non-zero, or
    # 'b' is not divisible by 'a', leading to no integer solution
    print("no solution")
elif a != 0 and b % a == 0:
    # Case where 'a' is non-zero and 'b' is divisible by 'a',
    # providing a single integer solution for 'x'
    print(b // a)
