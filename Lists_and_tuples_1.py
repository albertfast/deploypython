# Lesson code of List - 1 lesson
# Please compare this with your code. Run this and mess with this code.

# ============ Slide #: 3: Lists: creation  =========
print("\nSlide #: 3: Lists: creation")
print('empty_list = ', [])
a_list = [1, 2, "Python", 2.5]
print('a_list = ', a_list)
print('list(range(4)) = ', list(range(4)))
print('list("Code") =',list("Code"))

# ============ Slide #: 4: Lists: nested lists  =========
print("\nSlide #: 4: Lists: nested list")
a_list = [1, 2, [2, 3, 'o'], 4, 5]
print('a_list = ',  a_list)
print('a_list[2] = ', a_list[2])

# ============ Slide #: 5: Lists: length  =========
print("\nSlide #: 5: Lists: length")
print("len( [1, 2, [2, 3, 'o'],4, 5] ) = ", len( [1, 2, [2, 3, 'o'],4, 5] ))

# ============ Slide #: 6: Lists: accessibility  =========
print("\nSlide #: 6: Lists: accessibility")
py = ["Python", 2.5, 3]
print('py[1] = ', py[1])
print('py[-1] = ', py[-1])
li = [2, [3, 5], 6]
print('li[1][0] = ',  li[1][0])

# ============ Slide #: 7: Lists: membership  =========
print("\nSlide #: 7: Lists: membership")
li = [2, [3, 5], 6]
print("5 in li = ", 5 in li )
print("5 not in li = ",5 not in li)

# ============ Slide #: 8: Lists: iteration  =========
print("\nSlide #: 8: Lists: iteration")
for characters in sorted("Python"):  # sorted returns a list
    print(characters, end=", ")

# ============ Slide #: 9: Lists: iteration  =========
print("\n\nSlide #: 9: Lists: iteration")
a_list = [1, 2, 3, 4]
for indexes in range(len(a_list)):
    print(a_list[indexes] ** 2, end=", ")

# ============ Slide #: 10: Lists: iteration  =========
print("\n\nSlide #: 10: Lists: iteration")
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0  # need for creating the boolean expression
while count < len(a_list):
    print(a_list[count], end=", ")
    count += 1

# ============ Slide #: 11: Lists: iteration  =========
print("\nSlide #: 11: Lists: iteration")
# ================================UMPIRE========================================
# Understand:
# Problem: Given any list, write a Python program to return
# the sum of all the numbers in a list using a for loop. For
# example, give the list [1, 2, 3.5, "code", 'P'] your
# function must return 6.5.
# input = any list
# output = sum of numbers inside
# Ex. [1, 2, 3.5, "code", 'P'] -> 1 + 2+ 3.5
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

a_list = [1, 2, 3.5, "code", 'P']
sum2 = 0
for items in a_list:
    if isinstance(items, int) or isinstance(items, float):
        sum2 += items

print("The sum of numerics in ", a_list, " via regular iteration is: ", sum2)


# ============ Slide #: 13: Lists: comprehension  =========
print("\nSlide #: 13: Lists: comprehension")
a_list = [1, 2, 3.5, "code", 'P']
# sum2 = 0
# for items in a_list:
#     if isinstance(items, int) or isinstance(items, float):
#         sum2 += items
print("The sum of numerics in ", a_list, " via list comprehension is: ", sum([ items for items in a_list if isinstance(items, int) or isinstance(items, float)]))

# ============ Slide #: 14: Lists: mutability  =========
print("\nSlide #: 14: Lists: mutability")
list1 = [1, 2]
print("Id before item reassignment: ",id(list1), list1)
list1[1] = 5 # a mutability test
print("Id after item reassignment with list1[1] = 5: ",id(list1), list1) # ids will be same

list2 = [1, 2]
print("Id before reassignment: ", id(list2), list2)
list2 = [1, 2, 3] # not a mutability test
print("Id after reassignment with list2 = [1, 2, 3]: ", id(list2), list2) # ids will not be same

# ============ Slide #: 15: Tuples: introduction  =========
print("\nSlide #: 15: Tuples: introduction")
tp1 = 1, 2, 3
print('tp1 = ', tp1)
tp2 = (1, 2, 3)
print('tp2 = ', tp2)
tp3 = 3  # not a tuple
print('type(tp3) = ', type(tp3))
tp3 = (3)  # not a tuple!
print('type(tp3) = ',type(tp3))
tp3 = (3,)  # a tuple! how to create a tuple with one value
print('a tuple with one value, type(tp3) = ', type(tp3))
print('a tuple with one value, tp3 = ', tp3)

t1 = (1, 2, 3, [4, 5])
print('t1[3] = ', t1[3] )
print('t1 before t1[3][1] = 0: ', t1)
t1[3][1] = 0
print('t1 after t1[3][1] = 0: ', t1)
# t1[3] = 5  # TypeError: 'tuple' object does not support item assignment


# ============ Slide #: 17: Tuples: tuple assignment  =========
print("\nSlide #: 17: Tuples: tuple assignment")
# (1, 2, 'o')
(vr1, vr2, vr3) = (1, 2, 'o')  # tuple assignment
print('vr1, vr2, vr3 are: ', vr1, vr2, vr3)
print('vr1 =', vr1)
# uncomment and run
#(vr1, vr2, vr3) = (1, 'o')  # ValueError: not enough
# values to unpack (expected 3, got 2)
print('Originals, (vr1, vr3) =', (vr1, vr3))
(vr1, vr3) = (vr3, vr1)  # swapping vr1 and vr3
print('Swapped, (vr1, vr3) =', (vr1, vr3))
