# List of values from 1 to 10
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Anonymous function to find the maximum of two values
# Importing the reduce function from functools module
from functools import reduce

# Using reduce to find the maximum value in the list with a lambda function
# - The lambda function here takes two parameters, 'a' and 'b'.
# - The function returns 'a' if 'a' is greater than 'b'; otherwise, it returns 'b'.
# - reduce() applies the lambda function cumulatively to the elements of the list:
#   - Starts with the first two elements of the list: (1, 2), and returns 2 (the maximum).
#   - Then takes 2 and the next element (3), and returns 3.
#   - Repeats this process until all elements have been processed, resulting in the maximum value.
maxMyList = reduce(lambda a, b: a if a > b else b, myList)
print("maxMyList is", maxMyList)

# 2. Anonymous function to square each element in myList
# Using map with a lambda function that squares each element
# - The lambda function takes a single parameter 'x' and returns 'x * x' (the square of 'x').
# - map() applies this lambda function to each element of 'myList' and returns an iterable.
# - list() is used to convert the iterable returned by map() into an actual list.
return_results = list(map(lambda x: x * x, myList))
print("return_results is", return_results)
