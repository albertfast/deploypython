import packages as pkg
from functools import reduce


def do_sum(x1, x2):
    return x1 + x2


print("using reduce ==> ",reduce(do_sum, [1, 2, 3, 4]))

# Renaming functions to follow PEP 8 naming conventions
pkg.SayHello("Ahmet")


# Extracted functions to avoid repetition
def print_results(a, b):
    print("sum:", pkg.sum(a, b))
    print("average:", pkg.average(a, b))
    print("power:", pkg.power(a, 2))


print_results(10, 20)
pkg.playText()

pkg.laddMoney()
pkg.AddMoney()
pkg.filterAges(17)

def do_sum(x1, x2):
    return x1 + x2

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[3:]:
        first = func(first, i)
    return first

print("from last element after 2 elements later do_sum ==> ",my_reduce(do_sum, [1, 2, 12, 16]))

# Finding the area of a triangle
triangle = lambda m,n : 1/2 * m * n
res=triangle(34,24)
print("Area of the triangle: ",res)

series = [23,45,57,39,1,3,95,3,8,85]
result = filter (lambda m: m > 29, series)
print('All the numbers greater than 29 in the series are :',list(result))

# printing the cube of numbers given in the list
series = [23,5,1,7,45,9,38,65,3]
result = map (lambda m: m*m*m, series)
print('The cube of each element in the list are :',list(result))

# printing the sum of numbers given in the list from functools
from functools import reduce
series = [23,5,1,7,45,9,38,65,3]
sum = reduce (lambda m,n: m+n, series)
print('The total sum of all the elements in the list is :',sum)