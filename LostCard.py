# Purpose:
# To understand and practice for loops in Python.
#
# Problem Statement:
# There was a set of cards with numbers from 1 to N. One of the cards is now lost.
# Determine the number on that lost card given the numbers for the remaining cards.
#
# Given a number N, followed by N − 1 integers representing the numbers on the remaining cards
# (distinct integers in the range from 1 to N). Find and print the number on the lost card.

number = int(input())
expected_sum = (number * (number +1)) // 2
actual_sum =0
for _ in range(number-1):
    actual_sum += int(input())
lost_card = expected_sum - actual_sum
print(lost_card)

