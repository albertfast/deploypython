# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers,
# find the maximal element and print its row number and column number.
# If there are many maximal elements in different rows, report the one with smaller row number.
# If there are many maximal elements in the same row, report the one with smaller column number.

# Understand
# Task:
# 1. Parse a 2D matrix of integers (rows and columns are given as input).
# 2. Find the maximum element in the matrix.
# 3. Return the row index and column index of the first occurrence of the maximum element.

# Restriction
# 1. The matrix is guaranteed to have exactly m rows and n columns, as per the input.
# 2. Only basic Python functionalities (e.g., max, range, list comprehension) can be used.
# 3. The solution must handle edge cases like:
#    - Multiple maximum elements in different rows (choose the smallest row index).
#    - Multiple maximum elements in the same row (choose the smallest column index).
# 4. List comprehension should be used for processing the matrix.
# 5. No additional libraries or complex data structures can be used.

# Match
# 1. Parse inputs for a 2D list.
# 2. Use list comprehension instead of nested loops for matrix processing.
# 3. Keep track of the maximum element and its position.

# Plan
# 1. Parse the input to extract the number of rows (m) and columns (n).
# 2. Use list comprehension to build the 2D matrix from user input.
# 3. Flatten the 2D matrix into a list of tuples containing each element and its coordinates (row, column).
# 4. Use Python's max() function with a custom key to find the maximum value and its position.
# 5. Print the position of the maximum value.

# Implementation:
'''
def find_max_element_position():
    """
    Finds the position of the maximal element in a 2D list
    using list comprehension.

    Returns:
    - A tuple (row, column) indicating the position of the maximal element.
    """
    # Step 1: Read dimensions of the matrix
    m, n = map(int, input("Enter matrix dimensions (rows columns): ").split())

    # Step 2: Read the matrix using list comprehension
    matrix = [list(map(int, input().split())) for _ in range(m)]

    # Step 3: Flatten the matrix into a list of (value, row, column)
    elements_with_positions = [
        (matrix[row][col], row, col)  # Create tuples with value and its position
        for row in range(m)
        for col in range(n)
    ]

    # Step 4: Find the maximum element and its position
    max_element = max(elements_with_positions, key=lambda x: x[0])

    # Step 5: Extract row and column indices
    _, max_row, max_col = max_element

    # Step 6: Print the result
    print(max_row, max_col)

# Main program execution
if __name__ == "__main__":
    find_max_element_position()

'''
def find_max_element_position(matrix):
    """
    Finds the position of the maximal element in a 2D list.

    Parameters:
    - matrix: A list of lists representing the 2D matrix.

    Returns:
    - A tuple (row, column) indicating the position of the maximal element.
    """
    max_value = float('-inf')  # Başlangıçta en düşük değeri atanır
    max_position = (0, 0)  # Maksimum elemanın pozisyonu (satır, sütun)

    # Matrisin tüm elemanlarını kontrol et
    for i in range(len(matrix)):  # Satırlar üzerinde iterasyon
        for j in range(len(matrix[i])):  # Sütunlar üzerinde iterasyon
            if matrix[i][j] > max_value:  # Eğer mevcut eleman daha büyükse
                max_value = matrix[i][j]
                max_position = (i, j)  # Pozisyonu güncelle

    return max_position


# Kullanıcıdan girişleri al ve matrisi oluştur
def main():
    # İlk satır: Satır ve sütun sayısını oku
    m, n = map(int, input("Matrisin boyutlarını gir (satır sütun): ").split())
    matrix = []

    # Matrisin elemanlarını oku
    print("Matris elemanlarını satır satır girin:")
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Maksimum elemanın pozisyonunu bul
    max_pos = find_max_element_position(matrix)
    print(f"En büyük elemanın konumu: {max_pos[0]} {max_pos[1]}")


# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()
