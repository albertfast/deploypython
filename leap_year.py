# Given the year number. You need to check if this year is a leap year. If it is, print LEAP; otherwise, print COMMON.
# ===================== UMPIRE ====================
# Understand:
# Problem Statement:
# - Determine if a given year is a leap year or a common year based on the Gregorian calendar rules.
# - Print "LEAP" if it is a leap year, otherwise print "COMMON".

# Input:
# - year_input: An integer representing the year.

# Output:
# - "LEAP" if the year is a leap year.
# - "COMMON" if the year is not a leap year.

# Rules:
# - A year is a leap year if it is divisible by 4, but not divisible by 100.
# - However, a year is always a leap year if it is divisible by 400.

# Example input/output:
# - Input: 2000 -> Output: LEAP (since 2000 is divisible by 400)
# - Input: 1900 -> Output: COMMON (since 1900 is divisible by 100 but not 400)
# - Input: 2016 -> Output: LEAP (since 2016 is divisible by 4 and not by 100)
# - Input: 2019 -> Output: COMMON (since 2019 is not divisible by 4)

# Match:
# - Use conditional statements (if-else) to check divisibility conditions.
# - Apply logical operators for multiple conditions in a single line.

# Plan:
# 1. Check if the year is divisible by 4 and not by 100, or if it is divisible by 400.
# 2. If the condition is met, print "LEAP".
# 3. If the condition is not met, print "COMMON".

# Implementation:
year_input = int(input("Enter the year number: "))  # Step 1: Get user input for the year

# Step 2: Check if the year is a leap year according to the rules
if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
    # The year is a leap year if it meets the conditions
    print("LEAP")
else:
    # The year is not a leap year if it doesn't meet the conditions
    print("COMMON")
