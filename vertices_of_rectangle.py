# ===================== UMPIRE ====================

# Understand:
# Problem Statement:
# - Given three vertices of a rectangle whose sides are parallel to the coordinate axes,
#   we need to determine the coordinates of the fourth vertex.
# - Each rectangle has four vertices, and in this problem, we know three vertices.
# - Since the rectangle is aligned with the coordinate axes, the fourth vertex can be
#   found by identifying the unique x and y values among the given coordinates.

# Inputs:
# - Six integers representing the x and y coordinates of three vertices of the rectangle.
# - Each vertex consists of an (x, y) pair.

# Output:
# - The x and y coordinates of the fourth vertex as two integers.

# Match:
# - Use if/else statements or a list/set approach to find the unique x and y values.
# - Use sets to identify the values that appear only once, as they will represent the fourth vertex's coordinates.

# Plan:
# 1. Take six integer inputs representing the coordinates of three vertices.
# 2. Separate the x and y coordinates into two lists.
# 3. Identify the unique x and y values by checking which values appear only once.
# 4. Print the unique x and y values as the coordinates of the fourth vertex.

# Implementation:

# Input the coordinates of the three vertices
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))

# Store x and y values in separate lists
x_coords = [x1, x2, x3]
y_coords = [y1, y2, y3]

# Identify the unique x and y values for the fourth vertex
# Using list comprehension to find the value that appears once
fourth_x = [x for x in x_coords if x_coords.count(x) == 1][0]
fourth_y = [y for y in y_coords if y_coords.count(y) == 1][0]

# Output the coordinates of the fourth vertex
print("The coordinates of the fourth vertex are:")
print(fourth_x)
print(fourth_y)

#Short Way
# Initialize empty lists for x and y coordinates
x_coords = []
y_coords = []

# Use a for loop to get input for the three vertices
for i in range(3):
    x = int(input(f"Enter x{i + 1}: "))
    y = int(input(f"Enter y{i + 1}: "))
    x_coords.append(x)
    y_coords.append(y)
fourth_x = [x for x in x_coords if x_coords.count(x) == 1][0]
fourth_y = [y for y in y_coords if y_coords.count(y) == 1][0]
# Output the coordinates of the fourth vertex
print(fourth_x)
print(fourth_y)

