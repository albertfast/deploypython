# =====================Umpire===================
#Understand:
#Input = Given an integer,
#Output =  print its tens digit.
#Restriction = giving integer
# 1 = 0, 987 = 8 , 10 = 1
# (987%100) // 10

#Match: Sum of Digits , reminder mod

#Plan:
#1. Input Number
#2.  check greater than 9 or
#3. make calculation
#4. print the tens digit number
# a= int(input())
# print((a%100) // 10)

#Implementation:

while True:
    number = int(input())
    if number > 9:
        print((number % 100) // 10)
        break
    elif number < 10 and number > 0:
        print(0)
        break
    else:
        print('Invalid input. Please enter a number between 1 and 9999.')