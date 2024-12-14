import math
import statistics

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)
radii = [2, 5, 7.1, 0.3, 10, 16]

#Method 1: Direct method

areas =[]
for r in radii:
    a = area(r)
    areas.append(a)
print("areas: ", areas)

#Method 2: Use 'map' function
print(map(area, radii))
print(list(map(area, radii)))

# List of tuples with city names and temperatures in Celsius
temps = [
    ("Berlin", 29), 
    ("Cairo", 36), 
    ("Buenos Aires", 19),
    ("Los Angeles", 26), 
    ("Tokyo", 27), 
    ("New York", 28),
    ("London", 22), 
    ("Beijing", 32)
]

# Lambda function to convert Celsius to Fahrenheit
c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)

# Convert the temperatures and display the result as a list
converted_temps = list(map(c_to_f, temps))
print(converted_temps)


data = [1.3, 2.6, 6.7, -0.87 ,-9.6 , 6.3 ,-8.4]
avg = statistics.mean(data)
print("avg = ",avg)
print(list(filter(lambda x: x> avg, data)))
print(list(filter(lambda x: x< avg, data)))
# Calculate the median (middle value)
median = statistics.median(data)
print("Median =", median)

# Calculate the cube of each element
cubes = [x ** 3 for x in data]
print("cube = ", cubes)

data = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(list(data))
# Alt alta yazdırma
for triplet in data:
    print(triplet)
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)
for triplet in coloured_things:
    print(triplet)

multiples = []
for x in range(1,11):
    multiples.append(x*8)
print(multiples)

multiples = []
for x in range(1,11):
    multiples.append(x*8)
    print(multiples)

multiples = [x*8 for x in range(1,11)]
print(multiples)

