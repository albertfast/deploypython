# Combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

# Example usage
print(full_name("   leonhard", "EULER"))  # Output: 'Leonhard Euler'


# Define a function that builds a quadratic function
def build_quadratic_function(a, b, c):
    """
    Returns the function f(x) = ax^2 + bx + c
    Parameters:
    - a, b, c: Coefficients of the quadratic equation

    Returns:
    - A lambda function that represents the quadratic equation
    """
    return lambda x: a * x ** 2 + b * x + c


# Create a specific quadratic function f(x) = 2x^2 + 3x - 5
f = build_quadratic_function(2, 3, -5)

# Evaluate the function for different values of x
print(f"f(0) = {f(0)}")  # Expected output: -5
print(f"f(1) = {f(1)}")  # Expected output: 0
print(f"f(2) = {f(2)}")  # Expected output: 9

# Another example: build a function f(x) = 3x^2 + 1, then evaluate it for x = 2
result = build_quadratic_function(3, 0, 1)(2)
print(f"build_quadratic_function(3, 0, 1)(2) = {result}")  # Expected output: 13
