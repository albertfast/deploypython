# =====================Umpire===================
# Understand:
# Input = An integer a, representing the angle (in degrees)
# turned by the hour hand since midnight.
# Output = An integer representing the angle (in degrees)
# turned by the minute hand since the start of the current hour.
# Restriction = Both input and output are integers.

# Match:
# We know that the hour hand moves 30 degrees per hour (360 degrees / 12 hours).
# The minute hand moves 6 degrees per minute (360 degrees / 60 minutes).

# Plan:
# 1. Extract the angle within the current hour:
#    Use the modulus operation to get the angle within the current hour. This removes full rotations of 30 degrees (representing each hour).
# 2. Find the remaining angle after dividing by 30, which represents the part of the hour since the last hour mark.
#    This is done with `a % 30`, giving us the "extra" angle in the current hour.
# 3. Calculate the minute hand's angle:
#    Multiply the remaining angle by 12. This is because for each degree moved by the hour hand, the minute hand moves 12 degrees
#    (since 30 degrees for the hour hand corresponds to 360 degrees for the minute hand).
# 4. Print the calculated minute hand angle.
#   font=("Courier", 8, "normal"),  align="right"
# Implementation:

a = int(input())
minute_hand_angle = (a % 30) * 12
print( minute_hand_angle)
