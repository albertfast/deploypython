#Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday.
#An integer K in the range 1 to 365 is given. Find and print the number of day of week for
#K-th day of year provided that in this year January 1 was Thursday.
# Given = 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday.
#day_number
#January 1 was Thursday.
#Outout print day of week of day_number




#
#                                   /------------------7-----------------------/
#day     =  4,      5,      6,      0,     1,     2,     3,     4,     5,     6,     0,     1,     2,     3,     4,     5,     6, .....
#                                   ^      ^      ^
#                               (4+3)%7  (5+3)%7  (6+3)%7 .......
#day_no =       1,     2,     3,     4,     5,     6,     7,     8,     9,     10,     11, .......

#Match: %, sum of digits


#Plan:
#1.input day_number
#2.print(day_number + 3)%7

#implementation:
input_day = int(input())
print( (input_day + 3)%7)

