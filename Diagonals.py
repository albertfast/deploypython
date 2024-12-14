# Understand:
# The task is to create an n×n two-dimensional array (matrix) where the value of each cell
# is determined based on its distance from the main diagonal. The rules are as follows:
# - The main diagonal (where row index == column index) should have the value 0.
# - The diagonals adjacent to the main diagonal should have the value 1.
# - The next adjacent diagonals should have the value 2, and so on.
# The result is printed row by row, with values separated by spaces.

# Example:           input:                      Output:
#                    n = 5                       0 1 2 3 4
#                                                1 0 1 2 3
#                                                2 1 0 1 2
#                                                3 2 1 0 1
#                                                4 3 2 1 0

# Match:
# - Input: An integer n (size of the matrix).
# - Output: A printed n×n matrix where each cell's value depends on its distance from the main diagonal.
# - Constraints:
#   - n is a positive integer.

# Plan:
# 1. Read the integer input n for the size of the matrix.
# 2. Initialize an empty list matrix to hold the rows of the matrix.
# 3. For each row index i from 0 to n-1:
#    a. Create a new list row.
#    b. For each column index j from 0 to n-1:
#       - Calculate the value for the cell using abs(i - j) and append it to row.
#    c. Append the completed row to matrix.
# 4. Print each row of the matrix on a new line with values separated by spaces.

# Implementation:

def diagnol_matrix():
    # Read the size of the matrix
    n = int(input("Enter the size of the matrix (n): "))

    # Create the matrix based on the rule
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(abs(i - j))  # Fill the cell with the distance to the main diagonal
        matrix.append(row)

    # Print the matrix
    for row in matrix:
        print(*row)


# Call the function
diagnol_matrix()
