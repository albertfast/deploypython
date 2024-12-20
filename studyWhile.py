#For a given integer N, print all the squares of positive integers where the square is less than or equal to N, in ascending order.
# number = int(input("Enter a number: "))
# i = 1
# while True:
#     square = i ** 2
#     if square > number:
#         break
#     print(square, end=" ")
#     i += 1

# for i in range(5, 20):
#     print(i , end=" ") #5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

# for i in range(1, 15, 3):
#     print(i , end=" ") #1 4 7 10 13

# for i in range(15, 1, -2):
#      print(i , end=" ") #15 13 11 9 7 5 3

# A = "CA"
# B = "TX"
# for lc in A:
#     for rc in B:
#         print(lc, end=" ") #C C A A
#         print(lc + rc , end=" ") #CT CX AT AX
#         print(rc + lc, end=" ") #TC XC TA XA
        # C CT TC C CX XC A AT TA A AX XA

# n = int(input("Enter a number between 1 and 9: "))
# if 1 <= n  <=9:
#     for i in range(1, n + 1):
#         for k in range(1, i + 1):
#             print(k, end=" ")
#         print()

n = int(input("Enter a number between 1 and 9: "))
sum = 0
if 1 <= n  <=9:
    for i in range(1, n + 1):
        sum *= 10
        sum += i
        print(sum)
































