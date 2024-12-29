import math
import numpy as np
import matplotlib.pyplot as plt

class FunctionPlotter:
    """Represents a mathematical function for plotting."""
    def __init__(self, name, function, label, description):
        self.name = name
        self.function = function
        self.label = label
        self.description = description

    def plot(self, x_range=(-10, 10), num_points=400):
        x = np.linspace(*x_range, num_points)
        y = np.array([self.function(val) if val >= 0 else np.nan for val in x]) if "√" in self.label else self.function(x)

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

class FunctionManager:
    def __init__(self):
        self.functions = []

    def add_function(self, name, function, label, description):
        self.functions.append(FunctionPlotter(name, function, label, description))

    def get_function_names(self):
        return [func.name for func in self.functions]

    def get_function_by_name(self, name):
        for func in self.functions:
            if func.name == name:
                return func
        return None

# Instantiate the FunctionManager and add functions
function_manager = FunctionManager()
function_manager.add_function("absolute_value", lambda x: np.abs(x), "f(x) = |x|", "Absolute Value")
function_manager.add_function("linear", lambda x: x, "f(x) = x", "Linear")
function_manager.add_function("square_root", lambda x: np.sqrt(np.where(x >= 0, x, np.nan)), "f(x) = √x", "Square Root")
function_manager.add_function("quadratic", lambda x: x ** 2, "f(x) = x²", "Quadratic")
function_manager.add_function("quadratic_custom", lambda x: 2 * x ** 2 - 3 * x + 1, "f(x) = 2x² - 3x + 1", "Custom Quadratic")
function_manager.add_function("cubic", lambda x: x ** 3, "f(x) = x³", "Cubic")
function_manager.add_function("cube_root", lambda x: np.cbrt(x), "f(x) = ³√x", "Cube Root")
function_manager.add_function("reciprocal", lambda x: np.where(x != 0, 1 / x, np.nan), "f(x) = 1/x", "Reciprocal")
function_manager.add_function("reciprocal_squared", lambda x: np.where(x != 0, 1 / x ** 2, np.nan), "f(x) = 1/x²", "Reciprocal Squared")
