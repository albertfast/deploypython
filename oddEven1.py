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
'''
month = int(input("Enter the month number (1-12): "))

if month == 2:
    print(28)
elif month in {4, 6, 9, 11}:
    print(30)  # April, June, September, November have 30 days
elif 1 <= month <= 12:
    print(31)
else:
    print("Invalid Input")

'''
'''
# Dictionary to map each month to its days in 2017
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
    8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Enter the month number (1-12): "))

# Validate input and print the number of days
if 1 <= month <= 12:
    print(days_in_month[month])
else:
    print("Invalid Input")
'''
'''
# List of days in each month for 2017
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Enter the month number (1-12): "))

# Validate input and print the number of days
if 1 <= month <= 12:
    print(days_in_month[month])
else:
    print("Invalid Input")

'''