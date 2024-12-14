# ===================== Umpire ====================

# Understand:
# Input: A positive integer representing a year (e.g., 1401, 2017).
# Output: An integer representing the respective century of the given year.
# Restrictions: Both input and output should be integers.

# Match:
# Each century consists of 100 years.
# If a year ends in 00 (e.g., 1900, 2000), it belongs to that century (19th, 20th, etc.).
# However, for other years (e.g., 1901), we calculate the century by moving to the next century number.
# Example: 1901 is in the 20th century, while 1900 is in the 19th century.

# Plan:
# 1. Get the year as input from the user.
# 2. Calculate the century:
#    - Subtract 1 from the year and divide by 100.
#    - Adding 1 to the result ensures that we count the correct century for all years.
#    - Formula: (year - 1) // 100 + 1
# 3. Print the calculated century.

# Implementation:

# Get the year as input from the user
year = int(input("Enter the year: "))

# Calculate the century
correct_century = (year - 1) // 100 + 1

# Print the result
print("Century:", correct_century)
