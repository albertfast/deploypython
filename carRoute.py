# =====================Umpire===================
#Understand:
#Input = A car can cover a distance of N kilometers per day.
#Input = route of length M kilometers
#Output =  remaining days
#Restriction = integer
# N = 10, M = 81 , number_days = (81 + 10 - 1) // 10
#number_of_days = (M + N - 1) // N
#print(number_of_days)

#Match:

#Plan:
#1. Input Number
#2.  check INTEGER
#3. CALCULATE
#4. print the number_day

#Implementation:
N = int(input())
M = int(input())
number_of_days = (M + N - 1) // N
print(number_of_days)