number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 == number2 == number3:
    print(3)
elif number1 != number2 and number2 != number3 and number1 != number3:
    print(0)
else:
    print(2)
