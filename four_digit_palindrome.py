#Let's call an integer a palindrome if it remains the same after reading its digits from right to left.
# Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
# ===================== UMPIRE ====================

# Understand:
# Problem Statement: Read four digit integer if it palindrome print YES otherwise print NO
# If so, print "YES"; otherwise, print "NO".
# Example input/output:
# Input: 1221 --> Output: YES
# Input: 2553 --> Output: NO

# Input: A four-digit integer (X).
# Output: "YES" if the digits are unique and in ascending order, otherwise "NO".
# Restrictions: The input must be a four-digit number

# Match:
# Use basic conditional checks for  order of digits.
#  list, list compilation, take every element indivucial , == ,

# Plan:
# 1. Verify that the input number is a four-digit integer.
# 2. Check first element and last element and second element with 3rd element same.
# 3. Print "YES" if conditions are met; otherwise, print "NO".

# Implementation:
four_digit = int(input())
four_digit_str = str(four_digit)
four_digit_list = [int(d) for d in four_digit_str]
first_element = four_digit_list[0]
second_element = four_digit_list[1]
third_element = four_digit_list[2]
fourth_element = four_digit_list[3]
if 1000 <= four_digit <= 9999:
    if (first_element == fourth_element) and (second_element == third_element):
        print("YES")
    else:
        print("NO")


# Read the input as an integer
#four_digit = int(input())

# Verify that the input number is a four-digit integer
#if 1000 <= four_digit <= 9999:
    # Convert the integer to a string
    #four_digit_str = str(four_digit)

    # Check if the string is the same when reversed
    #if four_digit_str == four_digit_str[::-1]:
        #print("YES")
    #else:
        #print("NO")
#else:
    #print("NO")

