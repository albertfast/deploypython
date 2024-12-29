# Given lists
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]

# 1. List comprehension to multiply all elements in A by 7
# This list comprehension iterates over each element 'x' in list A and multiplies it by 7.
# The resulting list is stored in variable S.
S = [x * 7 for x in A]
print("S is", S)

# 2. List comprehension to find unique even elements in both A and B
# This list comprehension iterates over each element 'x' in the combined list (A + B).
# It checks if 'x' is even by using the condition (x % 2 == 0). If true, it adds 'x' to the set.
# The use of set ensures that only unique values are kept.
Even = sorted(list({x for x in A + B if x % 2 == 0}))
# The 'sorted()' function is used to make sure the final list is in ascending order.
# The 'list()' function converts the set back into a list format for printing.
print("Even is", Even)

# 3. List comprehension to multiply each element in A with each element in B
# This nested list comprehension iterates over each element 'a' in A and each element 'b' in B.
# It multiplies 'a' by 'b' and adds the result to the 'multiples' list.
multiples = [a * b for a in A for b in B]
print("multiples is", multiples)  

