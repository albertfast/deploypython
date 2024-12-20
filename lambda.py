import matplotlib.pyplot as plt
import numpy as np

# Example 1: Basic Lambda Function for 3x + 1
f1 = lambda x: 3 * x + 1
print("f1(x) = 3x + 1")
print(f"Testing f1 with x = 2: f1(2) = 3 * 2 + 1 = {f1(2)}")  # Expected output: 7

# Example 2: Lambda Function with Variable Input
x_value = 6
print(f"\nTesting f1 with x = {x_value}: f1({x_value}) = 3 * {x_value} + 1 = {f1(x_value)}")  # Expected output: 19

# Example 3: Lambda within a Regular Function
def f2(y):
    return lambda x: (y ^ int(x)) + 7  # Ensure 'x' is cast to integer for XOR

print("\nf2(y)(x) = y ^ x + 7, where ^ is the XOR operation.")
y_value, x_value = 2, 3
print(f"Testing f2 with y = {y_value} and x = {x_value}: f2(2)(3) = 2 ^ 3 + 7 = {f2(y_value)(x_value)}")  # Expected output: 8

# Explanation of the functions:
print("\nExplanation:")
print("1. f1(x) = 3 * x + 1: This is a linear function with a slope of 3 and y-intercept at 1.")
print("2. f2(y)(x) = y ^ x + 7: This function uses the XOR bitwise operation between y and x, and adds 7 to the result.")

# Now let's plot these functions and a few others to visualize them
# Define a list of lambda functions and their descriptions for plotting
lambda_functions = [
    (lambda x: 3 * x + 1, "f1(x) = 3x + 1"),
    (lambda x: 2 * x + 5, "f3(x) = 2x + 5"),
    (lambda x: -x + 10, "f4(x) = -x + 10"),
    (lambda x: x ** 2, "f5(x) = x^2"),
    (lambda x: x ** 3, "f6(x) = x^3"),
    (lambda x: np.sqrt(x) if x >= 0 else np.nan, "f7(x) = sqrt(x)"),  # Handle negative values in sqrt
    (lambda x: np.abs(x), "f8(x) = |x|"),
    (lambda x: np.sin(x), "f9(x) = sin(x)"),
    (lambda x: int(x) ^ 1 + 7, "f10(x) = int(x) ^ 1 + 7")  # Cast to int for XOR
]

# Plot each function on the x-y plane
x = np.linspace(-10, 10, 400)  # Define x values from -10 to 10

plt.figure(figsize=(14, 10))
for func, label in lambda_functions:
    # Handle cases where x values may go out of domain (e.g., sqrt of negative numbers)
    try:
        y = np.array([func(val) for val in x])  # Evaluate function element-wise
        plt.plot(x, y, label=label)
    except ValueError as e:
        print(f"Skipping {label} due to domain error: {e}")

# Customize plot
plt.title("Graphs of Different Lambda Functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
