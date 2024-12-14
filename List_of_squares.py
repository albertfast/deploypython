#For a given integer N, print all the squares of positive integers where the square is less than or equal to N, in ascending order.
# ================================UMPIRE========================================
# Understand:         Input:            Output:
#                      50               1 4 9 16 25 36 49
#                      10               1 4 9
#                      9                1 4 9
#                      8                1 4
#                      4                1 4
#                      1                1
#                      100              1 4 9 16 25 36 49 64 81 100
#                      99               1 4 9 16 25 36 49 64 81

number = int(input())
square_root = int(number ** 0.5)
i = 1
while True:
    square = i ** 2
    if square > number:
        break
    print(square, end=" ")
    i += 1
