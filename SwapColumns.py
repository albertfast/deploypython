# Understand:
# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers,
# followed by two non-negative integers i and j less than n, swap the columns i and j of 2d list and print the result.
# Example:                      Input:                Output:
#                               3 4
#                               11 12 13 14           12 11 13 14
#                               21 22 23 24           22 21 23 24
#                               31 32 33 34           32 31 33 34
#                               0 1

# Match : Scale, Matrix
# Plan:

def swap_columns():
    m, n = map(int, input("Enter number of rows and columns (m n): ").split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    i1, i2 = map(int, input("Enter number of index for swap (i1 i2): ").split())
    result = []
    for row in matrix:
        row[i1], row[i2] = row[i2], row[i1]
        result.append(row)
    for row in result:
        print(*row)
swap_columns()