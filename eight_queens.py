# It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other.
# Thus, it requires that no two queens share the same row, column, or diagonal.

# Given a placement of 8 queens on the chessboard, if there is a pair of queens that violates this rule,
# print YES, otherwise print NO. The input consists of eight coordinate pairs, one pair per line,

# UNDERSTAND:
# The goal is to check if 8 queens on a chessboard are placed such that no two queens threaten each other.
# This means no two queens can be on the same row, column, or diagonal.
# Input: Two lists x and y representing the positions of queens on an 8x8 chessboard.
# Output: Print "YES" if any two queens threaten each other, otherwise print "NO".

# MATCH:
# This problem matches the "conflict detection" category, where we check for specific constraints.
# Constraints:
# 1. No two queens share the same row: x-coordinates must be unique.
# 2. No two queens share the same column: y-coordinates must be unique.
# 3. No two queens share the same diagonal:
#    - Diagonal condition 1: x[i] - y[i] must be unique for all queens.
#    - Diagonal condition 2: x[i] + y[i] must be unique for all queens.

# Initialize the inputs
# x = [1, 2, 3, 4, 5, 6, 7, 6]  # Row positions of the queens
# y = [5, 3, 1, 7, 2, 5, 6, 4]  # Column positions of the queens

# PLAN:
# 1. Use two lists x and y to store the positions of queens.
# 2. Iterate through the input to populate these lists.
# 3. Check if all constraints are satisfied:
#    - Rows (x), columns (y), and diagonals are unique.
# 4. Return "YES" if any constraint is violated, otherwise return "NO".

'''
def check_queens_chessboard(x, y):
    # IMPLEMENTATION:
    # Use sets to check uniqueness for rows, columns, and diagonals.
    rows = set()
    cols = set()
    diag1 = set()  # Diagonal condition 1: x - y
    diag2 = set()  # Diagonal condition 2: x + y

    for i in range(8):
        # If any constraint is violated, return "YES"
        if x[i] in rows or y[i] in cols or (x[i] - y[i]) in diag1 or (x[i] + y[i]) in diag2:
            return "YES"

        # Add current queen's position to the sets
        rows.add(x[i])
        cols.add(y[i])
        diag1.add(x[i] - y[i])
        diag2.add(x[i] + y[i])

    # If no violations, return "NO"
    return "NO"


# Input: Reading positions of 8 queens
x = []  # List to store x-coordinates (rows)
y = []  # List to store y-coordinates (columns)
for i in range(8):
    # Split input and parse as integers for x and y
    a_list = [int(s) for s in input().split()]  # Use list comprehension to get input data
    x.append(a_list[0])  # Append x-coordinate
    y.append(a_list[1])  # Append y-coordinate

# Output: Check and print if queens threaten each other
print(check_queens_chessboard(x, y))
'''
# Plan
# 1. input = x, y
# 2. init yesno = 'no'
# 3. for i from 1 to 8
#   3.1 for j from i + 1 to 8:
#       3.1.1 x[i] == or y[j] == abs(x[i] - x[j]) == abs(y[i] - y[j])
# 4. return NO

def check_queens(x,y):
    """Returns YES if two queens share row or column on diagonal otherwise returns NO """
    for i in range(8):
        for j in range(i+1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return  "YES"
    return "NO"

def main():
    # x = [1, 2, 3, 4, 5, 6, 7, 8]
    # y = [5, 3, 1, 7, 2, 8, 6, 4]
    #
    # print(check_queens(x, y))
    x = []
    y = []
    for inputs in range(8):
        a_list = [int(s) for s in input().split()]  # Use list comprehension to get input data
        x.append(a_list[0])
        y.append(a_list[1])

    print(check_queens(x, y))

if __name__ == "__main__":
    main()




























