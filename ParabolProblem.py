import numpy as np

# Define the vertex and the symmetric point calculation
vertex_x = 3 / 5


# Function to calculate corresponding x2 for given x1
def get_x2(x1):
    return 6 / 5 - x1


# Define the roots for some values of x1
x1_values = np.linspace(-10, 10, 400)
x2_values = get_x2(x1_values)


# Determine the coefficient of the parabola y = a(x-x1)(x-x2)
def get_parabola_coeffs(x1, x2):
    a = 1  # Assume coefficient of leading term is 1 for simplicity
    b = -(x1 + x2)  # Coefficient of x
    c = x1 * x2  # Constant term
    return a, b, c


# Function to get the y value at vertex for respective x1, x2
def get_y_vertex(a, b, c, x_vertex):
    return a * x_vertex ** 2 + b * x_vertex + c


# Solve for x1 such that the y value at the vertex is zero
solutions = []
for x1 in x1_values:
    x2 = get_x2(x1)
    a, b, c = get_parabola_coeffs(x1, x2)
    y_vertex = get_y_vertex(a, b, c, vertex_x)
    if np.isclose(y_vertex, 0, atol=1e-6):
        solutions.append((x1, x2))

# Display the solutions
print("Solutions (x1, x2):", solutions)
