daysInMonth_2017 = int(input())

if daysInMonth_2017 > 0 and daysInMonth_2017 <= 7:
   if daysInMonth_2017 % 2 == 1:
      print(31)
   elif daysInMonth_2017 == 2:
      print(28)
   else:
      print(30)
elif daysInMonth_2017 > 7 and daysInMonth_2017 <= 13:
    if daysInMonth_2017 % 2 == 0:
        print(31)
    else:
        print(30)
else:
    print("Invalid Input")