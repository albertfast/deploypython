# ================================ UMPIRE =======================================
# Understand:
# The task is to create an n×n two-dimensional array (matrix) where the value of each cell
# is determined based on the following rules:
# - On the anti-diagonal (where row index + column index == n - 1), put the value 1.
# - On the diagonals above the anti-diagonal, put the value 0.
# - On the diagonals below the anti-diagonal, put the value 2.
# The result is printed row by row, with values separated by spaces.

# Example:
# Input: n = 4
# Output:
# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
# 1 2 2 2

# Match:
# - Input: An integer n (size of the matrix).
# - Output: A printed n×n matrix where each cell's value is determined based on the above rules.
# - Constraints:
#   - n is a positive integer.

# Plan:
# 1. Read the integer input n for the size of the matrix.
# 2. Initialize an empty list matrix to hold the rows of the matrix.
# 3. For each row index i from 0 to n-1:
#    a. Create a new list row.
#    b. For each column index j from 0 to n-1:
#       - Determine the value based on the following:
#         - If i + j == n - 1: Append 1 (anti-diagonal).
#         - If i + j < n - 1: Append 0 (above the anti-diagonal).
#         - If i + j > n - 1: Append 2 (below the anti-diagonal).
#    c. Append the completed row to matrix.
# 4. Print each row of the matrix on a new line with values separated by spaces.

# Implementation:
def diagnol_matrix():
    n = int(input())

    # Create the matrix based on the rule
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i + j == n - 1:  # Anti-diagonal
                row.append(1)
            elif i + j < n - 1:  # Above the anti-diagonal
                row.append(0)
            else:  # Below the anti-diagonal
                row.append(2)
        matrix.append(row)

    for row in matrix:
        print(*row)

diagnol_matrix()
