import math
import matplotlib.pyplot as plt
import numpy as np

class Function:
    """Represents a mathematical function for plotting."""
    def __init__(self, name, function, label, description):
        self.name = name
        self.function = function
        self.label = label
        self.description = description

    def plot(self, x_range=(-10, 10), num_points=400):
        """Plots the function using matplotlib."""
        x = np.linspace(x_range[0], x_range[1], num_points)
        try:
            y = self.function(x)
        except ValueError: #Handles functions that might raise ValueErrors (e.g., sqrt of negative numbers)
            y = np.array([self.function(val) if val >= 0 else np.nan for val in x]) if "sqrt" in self.name else np.nan # Improved NaN handling

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=self.label)
        plt.title(f"{self.description} Function")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True)
        plt.show()

    def __str__(self):
        return f"Function: {self.label}\nDescription: {self.description}"

# Define functions as Function objects
functions = {
    "absolute_value": Function("absolute_value", lambda x: np.abs(x), "f(x) = |x|", "Absolute Value"),
    "linear": Function("linear", lambda x: x, "f(x) = x", "Linear"),
    "square_root": Function("square_root", lambda x: np.sqrt(x), "f(x) = √x", "Square Root"),
    "quadratic": Function("quadratic", lambda x: x ** 2, "f(x) = x²", "Quadratic"),
    "quadratic_custom": Function("quadratic_custom", lambda x: 2 * x ** 2 - 3 * x + 1, "f(x) = 2x² - 3x + 1", "Custom Quadratic"),
    "cubic": Function("cubic", lambda x: x ** 3, "f(x) = x³", "Cubic"),
    "cube_root": Function("cube_root", lambda x: np.cbrt(x), "f(x) = ³√x", "Cube Root"),
    "reciprocal": Function("reciprocal", lambda x: np.where(x != 0, 1 / x, np.nan), "f(x) = 1/x", "Reciprocal"),
    "reciprocal_squared": Function("reciprocal_squared", lambda x: np.where(x != 0, 1 / x ** 2, np.nan), "f(x) = 1/x²", "Reciprocal Squared")
}



# import math
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Dictionary holding all functions, their labels, and descriptions
# functions = {
#     "absolute_value": {
#         "function": lambda x: np.abs(x),
#         "label": "f(x) = |x|",
#         "description": "Absolute Value"
#     },
#     "linear": {
#         "function": lambda x: x,
#         "label": "f(x) = x",
#         "description": "Linear"
#     },
#     "square_root": {
#         "function": lambda x: np.sqrt(np.where(x >= 0, x, np.nan)),  # Ensure sqrt only gets non-negative values
#         "label": "f(x) = √x",
#         "description": "Square Root"
#     },
#     "quadratic": {
#         "function": lambda x: x ** 2,
#         "label": "f(x) = x²",
#         "description": "Quadratic"
#     },
#     "quadratic_custom": {
#         "function": lambda x: 2 * x ** 2 - 3 * x + 1,  # Example: 2x² - 3x + 1
#         "label": "f(x) = 2x² - 3x + 1",
#         "description": "Custom Quadratic"
#     },
#     "cubic": {
#         "function": lambda x: x ** 3,
#         "label": "f(x) = x³",
#         "description": "Cubic"
#     },
#     "cube_root": {
#         "function": lambda x: np.cbrt(x),
#         "label": "f(x) = ³√x",
#         "description": "Cube Root"
#     },
#     "reciprocal": {
#         "function": lambda x: np.where(x != 0, 1 / x, np.nan),
#         "label": "f(x) = 1/x",
#         "description": "Reciprocal"
#     },
#     "reciprocal_squared": {
#         "function": lambda x: np.where(x != 0, 1 / x ** 2, np.nan),
#         "label": "f(x) = 1/x²",
#         "description": "Reciprocal Squared"
#     }
#     # "mathOlympiadQuestion": {
#     #     "function": lambda x: np.where(((1 + math.sqrt(5))/2)**12, np.nan),
#     #     "label": "((1 + math.sqrt(5))/2)**12",
#     #     "description": "Math Olympiad Question"
#     # }
# }
#
#
# # Function to plot a specific graph based on the selected function name
# def plot_function(func_name):
#     if func_name not in functions:
#         print("Invalid function name. Available functions are:")
#         for name in functions:
#             print(f" - {name}")
#         return
#
#     func_info = functions[func_name]
#     func = func_info["function"]
#     label = func_info["label"]
#     description = func_info["description"]
#
#     # Define the range for x values
#     x = np.linspace(-10, 10, 400)
#     y = np.array([func(val) if val >= 0 else np.nan for val in x]) if "sqrt" in func_name else func(x)
#
#     # Plotting the graph
#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, label=label)
#     plt.title(f"{description} Function")
#     plt.xlabel("x-axis")
#     plt.ylabel("y-axis")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#     # Print information about the function
#     print(f"Function: {label}")
#     print(f"Description: {description}")
#
#
# # Example usage:
# # Call plot_function with the name of the function you want to plot.
# # You can change "linear" to any other function name defined in the dictionary.
# plot_function("quadratic_custom")

