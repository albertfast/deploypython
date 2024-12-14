# =====================Umpire===================
# Understand:
# Input =  Given an integer
# Output = print "odd" , print "even"
# int_ui = 5 5 % 2 = 1 ==> "odd"
# int_ui = 5 6 % 2 = 2 ==> "even"
# Restriction = print "odd" if it's odd and  print "even" otherwise.

# Match: if else statement, Compare last bit, ten digit, sum of digit
#int_ui % 2 == 1 => odd, int_ui % 2 == 0 => even

# Plan:
# 1. input int_ui
# 2. if int_ui % 2 == 1:
# 2.1   print("odd")
# 3. else:
# 3.1   print("even")

# Implementation:
int_ui = int(input())
if int_ui % 2 == 1:
    print("odd")
else:
    print("even")

# Read the input as an integer
four_digit = int(input())

# Verify that the input number is a four-digit integer
if 1000 <= four_digit <= 9999:
    # Convert the integer to a string
    four_digit_str = str(four_digit)

    # Check if the string is the same when reversed
    if four_digit_str == four_digit_str[::-1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


