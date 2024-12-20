bit_map = [i + 8 * j for i in range(8) for j in range(4)]
print(bit_map)

x = [i for i in range(5)]
print(x)

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)


# Define two strings
x = "Mother's Day May 12th"
y = "Father's Day June 16th"

# Split both strings into lists of words
x = x.split()
y = y.split()

# Global z: created as an empty list and filled later
z = [x[i] if not j else y[i] for i in range(len(x)) for j in range(2)]

# Print the global z
print("Global z before function call:", z)

# Create an empty list to store the merged result
#z = []
# Iterate through the length of the first list
# for i in range(len(x)):
#     # Append the corresponding words from both lists alternately
#     z.append(x[i])
#     z.append(y[i])
#
# # Print the final merged list
# print(z)
#print(" ".join(z))
# print("".join(list("qwerty")))


# Define a function with its own local z
def simple_func():
    # Local z inside the function
    z = [f"{x[i]}-{y[i]}" for i in range(len(x))]
    print("Local z inside the function:", z)
    return z
# Call the function
local_z = simple_func()

# Print the global z after function call
print("Global z after function call:", z)

# Print the returned local z from the function
print("Returned local z:", local_z)

# Print global z joined as a string
print("Global z joined:", " ".join(z))

a_list = [ 1, 2, [3, 4], 'Code']
print('a_list[+1] = ', a_list[1])
print('a_list[-3] = ', a_list[-3])
print('a_list[-2] return 4 = ', a_list[-2][1])
print('a_list[-1] = ', a_list[-1])
print('a_list[3][::-1] = ', a_list[3][::-1])
print('a_list[-1][-1] = ', a_list[-1][-1])

for itemList in a_list:
    print("For loop item list => ",itemList)
for position in range(len(a_list)):
    print("For loop position list => ",a_list[position])
for number in range(20):
    if number % 3 == 0:
        print(number, end= " ")

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)

alist = [4, 2, 8, 6, 5]
blist = [ ]
for item in alist:
    blist.append(item+5)
for character in sorted(alist):
    print(character, end=", ")

print("This is blist ==> ",blist)

print("\nSlide #: 8: Lists: iteration")
for character in sorted("Albert"):
    print(character, end=", ") # A, b, e, l, r, t,

# ============ Slide #: 9: Lists: iteration  =========
print("\n\nSlide #: 9: Lists: iteration")
coolList  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for indexes in range(len(coolList)):
    print(coolList[indexes] ** 2, end =", \n ")

c_list = [1, 2, [3, 4], 'Code']
count = 0
while count <len(c_list):
    print("While Count ==> ",c_list[count], end=", ")
    count += 1
for indexes in range(-1, -len(c_list)-1, -1 ):
    print(c_list[indexes], end=",\n ")

print("\nSlide #: 11: Lists: iteration")
# ================================UMPIRE========================================
# Understand:
# Problem: Given any list, write a Python program to return
# the sum of all the numbers in a list using a for loop. For
# example, give the list [1, 2.2, 3.5, "code", 'P'] your
# function must return 6.7.
# input = any list
# output = sum of numbers inside
# Ex. [1, 2.2, 3.5, "code", 'P'] -> 1 + 2+ 3.5
# Leave nne numeric types, check the type use isinstance
# Match: String iteration, accumulation
#
# Plan:
# 1. input a_list
# 2. init sum
# 3. for items in a_list:
#       3.1 if items is a number:
#              3.1.1 increment sum
# 4. return sum

# Implementation:

a_list = [1, 2.2, 3.5,"code", 'P']
sum2 = 0
for items in a_list:
    if isinstance(items, int) or isinstance(items, float):
    #if type(items) == int or type(items) == float:
        sum2 += items
print(sum([items for items in a_list if type(items) == int or type(items) == float]))
print("The sum of numerics in ", a_list, " via regular iteration is: ", sum2)

alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print("Last bList ",blist)

print("\nSlide #: 13: Lists: comprehension")
a_list = [6, 2, 3.5, "code", 'P']
# sum2 = 0
# for items in a_list:
#     if isinstance(items, int) or isinstance(items, float):
#         sum2 += items

print("The sum of numerics in ", a_list, " via list comprehension is: ", sum(items for items in a_list if isinstance(items, int) or isinstance(items, float)))


# Understand:
# Problem: Given a list of integers with duplicates, write a Python
# function to return a new list of numbers
# with duplicates removed. For example, given the lists
# [1, 2, 3, 2, 2, 1, 1, 3, 3] return [1, 2, 3]. In mathematics,
# a set is a collection of unique set of elements. So this is a classic
# set creation operation. However, since we are not yet there on Python
# sets, you are not allowed to use any set or dictionary operations here.
# Investigate how you can solve this using list comprehension.

# Input = Given a list of integers with duplicates
# Output = List of numbers with duplicates removed
# Restriction = We can't use sets

# ex
# a_list = [1, 2, 3, 2, 2, 1, 1, 3, 3] -> [1, 2, 3]
# set1 = [1, 2, 3]

# Plan:
# 1. input a_list
# 2. init. set to []
# 3. for items in a_list:
#   3.1 if items not in the set:
#       3.1.1 append items to set
#4. return set

# implementation:
def remove_duplicates(a_list):
    """ Returns duplicates removed from a list """
    set1 = []
    for items in a_list:
        if items not in set1:
            set1.append(items)
    return set1
def remove_duplicates2(a_list):
    set2 = []
    [set2.append(items) for items in a_list if items not in set2]
    return set2
a_list = [1, 2, 3, 3, 1, 2]

print(remove_duplicates(a_list))
print(remove_duplicates2(a_list))






















