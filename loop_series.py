# ================================UMPIRE========================================
# Understand:
# Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
# Input: 2 Integer A and B
# Output: print in range
# Example:                         Input:                     Output:
#                            A = 1     B = 10               1 2 3 4 5 6 7 8 9 10
#                            A = -3    B = 14               -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#                            A = 0     B = 0                0
#                            A = 5     B = 8               5 6 7 8

while True:
    A = input("Enter A (or type 'exit' to quit): ")
    if A.lower() == 'exit':
        break
    B = input("Enter B (or type 'exit' to quit): ")
    if B.lower() == 'exit':
        break

    try:
        A = int(A)
        B = int(B)

        if A <= B:
            for i in range(A, B + 1):
                print(i, end=" ")
            print()  # To move to the next line after printing the range
        else:
            print("Please enter A <= B input")
    except ValueError:
        print("Invalid input. Please enter integers for A and B.")
