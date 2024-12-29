# Function to square a number
def square(x):
    y = x * x  # Multiply x by itself
    print(f"square({x}) = {y} (This is {x} multiplied by itself)")
    return y

# Function to calculate the sum of squares of three numbers with additional steps
def sum_of_squares(x, y, z):
    a = square(x)  # Calculate square of the first number
    print(f"Step 1: First square calculated, a = {a} (This is the square of {x})")

    # Add the square of z to a (instead of x) for variety
    a += square(z)  # Recalculate square of z and add it to 'a'
    print(f"Step 2: Added square(z), new a = {a} (The square of {z} was added to a)")

    b = square(y)  # Calculate square of the second number
    print(f"Step 3: Second square calculated, b = {b} (This is the square of {y})")

    # Add the square of b to itself
    b += square(b)  # Recalculate square of b and add it to itself
    print(f"Step 4: Added square(b) to b, new b = {b} (The square of {b} was added to itself)")

    c = square(z)  # Calculate square of the third number
    print(f"Step 5: Third square calculated, c = {c} (This is the square of {z})")

    # Add the square of a to c
    c += square(a)  # Add square of a to c
    print(f"Step 6: Added square(a) to c, new c = {c} (The square of a was added to c)")

    # Print the individual squared values and their sum
    print(f"sum_of_squares({x}, {y}, {z}) = {a} + {b} + {c} = {a + b + c} (Adding all the squares together)")
    return a + b + c

# Values to square
a = -5
b = 2
c = 10

# Print initial values
print(f"Initial values: a = {a}, b = {b}, c = {c}")

# Calculate the sum of squares
result = sum_of_squares(a, b, c)

# Print the final result
print(f"Final result: {result} (The sum of squares of {a}, {b}, and {c})")
