#Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31)
# in the year 2017, print the month and the day of the next day to it.
# Example ==>  Input : MONTH      Input: DAY      Output: MONTH            DAY
#                        4                30               5                 1
#                        3                25               3                 26

#Match : Days In Month, If Else, List Comprehension

# Plan:
# 1. Take user input for Month and day in month
# 2. Check Month have how many days, if less than 28 days print same month + 1 day
# 3. if more than 28 days check this month have how many days
# 4. if input 4 month have  30 days print +1 month +1 day
# 5. if input 5 month and day 30 print 5 month 31 day

'''
monthIn_2017 = int(input("Enter the month: "))
daysInMonth_2017 = int(input("Enter the day: "))

if monthIn_2017 > 0 and monthIn_2017 <= 7:
   if (monthIn_2017 % 2 == 1) and (daysInMonth_2017 >= 31):
      print(f"{monthIn_2017 + 1}\n1")
   elif daysInMonth_2017 < 31:
       print(f"{monthIn_2017}\n{daysInMonth_2017 + 1}")
   elif (monthIn_2017 == 2) and (daysInMonth_2017 >= 28):
      print(f"{monthIn_2017 + 1}\n1")
   elif (monthIn_2017 == 2) and (daysInMonth_2017 < 28):
      print(f"{monthIn_2017}\n{daysInMonth_2017 + 1}")
   elif (monthIn_2017 % 2 == 0) and (daysInMonth_2017 >= 30):
      print(f"{monthIn_2017 + 1}\n1")
   elif daysInMonth_2017 < 30:
       print(f"{monthIn_2017}\n{daysInMonth_2017 + 1}")
elif monthIn_2017 > 7 and monthIn_2017 < 13:
    if (monthIn_2017 == 12) and (daysInMonth_2017 >= 31):
        print("1\n1")
    elif (monthIn_2017 % 2 == 0) and (daysInMonth_2017 >= 31):
        print(f"{monthIn_2017 + 1}\n1")
    elif (monthIn_2017 % 2 == 1) and (daysInMonth_2017 >= 30):
        print(f"{monthIn_2017 + 1}\n1")
    elif daysInMonth_2017 < 31:
        print(f"{monthIn_2017}\n{daysInMonth_2017 + 1}")
else:
    print("Invalid Input")
'''

# Days in each month for the year 2017
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Input: month and day
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))

# Check if the input is valid
if 1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]:
    # Check if it's the last day of the month
    if day == days_in_month[month - 1]:
        # Move to the first day of the next month
        day = 1
        month += 1
        # If it was December, reset to January
        if month == 13:
            month = 1
    else:
        # Otherwise, just move to the next day
        day += 1

    # Print the next day with each value on a new line
    print(f"{month}\n{day}")
else:
    print("Invalid Input")


