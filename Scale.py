# Understand:
# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers,
# followed by one integer c. Multiply every element by c, print the result, and find the position of the maximum element.

def find_max_element_position():
    # Read dimensions (m, n)
    m, n = map(int, input("Enter number of rows and columns (m n): ").split())

    # Read the 2D list
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Read the multiplier value (c)
    c = int(input("Enter the multiplier (c): "))

    # Multiply every element in the matrix by c and print the result
    result = []
    for row in matrix:
        result.append([element * c for element in row])

    # Print the updated matrix
    print("Updated Matrix:")
    for row in result:
        print(*row)

    # Find the position of the maximum element
    max_value = float('-inf')
    max_position = (-1, -1)
    for i in range(m):
        for j in range(n):
            if result[i][j] > max_value:
                max_value = result[i][j]
                max_position = (i, j)

    print(f"The maximum element is {max_value} at position {max_position} (0-indexed).")

# Call the function
find_max_element_position()
