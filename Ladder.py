# ================================UMPIRE========================================
# Understand:
# For a given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers
# from 1 to k without spaces between them. To do that, you can use the sep and end arguments for the function print().
# For example, for n = 4, your program must print,
#
# 1
# 12
# 123
# 1234

# Input n 1 <= n <= 9
# output above pattern

# Match: two by two for loop

# Plan:
# 1. input: n
# 2. for numbers from 1 to n:
#    2. for numbers2 from 1 to numbers times:
#      2.1 print numbers2
# Implementation:
# n = int(input("Enter a number between 1 and 9: "))
# if 1 <= n  <=9:
#     for i in range(1, n + 1):
#         for k in range(1, i + 1):
#             print(k, end=" ")
#         print()

# Plan2:
# 1. input: n
# 2. init sum
# 3. for i between 1 to n:
#       3.1 update sum with previous sum * 10
#       3.2 update sum with adding i
#       3.3 print()

n = int(input("Enter a number between 1 and 9: ")) # Example: 4
sum = 0                                            # Output:
if 1 <= n  <=9:                                    # 1
    for i in range(1, n + 1):                      # 12
        sum *= 10                                  # 123
        sum += i                                   # 1234
        print(sum)