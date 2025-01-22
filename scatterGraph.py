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

    def __call__(self, x):
        return self.function(x)

    def scatter_plot(self, x_range=(-10, 10), num_points=50):
        """Generates a scatter plot for the function."""
        # Define the range for x values
        x = np.linspace(x_range[0], x_range[1], num_points)
        try:
            y = self.function(x)
        except ValueError:
            # Handle cases like sqrt where inputs may lead to domain errors
            y = np.array([self.function(val) if val >= 0 else np.nan for val in x]) if "sqrt" in self.name else np.nan

        # Scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, label=self.label, color="red", alpha=0.7)
        plt.title(f"{self.description} Function")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True)
        plt.show()

functions = {
    "absolute_value": Function("absolute_value", lambda x: np.abs(x), "f(x) = |x|", "Absolute Value"),
    "linear": Function("linear", lambda x: x, "f(x) = x", "Linear"),
    "square_root": Function("square_root", lambda x: np.sqrt(x), "f(x) = √x", "Square Root"),
    "quadratic": Function("quadratic", lambda x: x ** 2, "f(x) = x²", "Quadratic"),
    "quadratic_custom": Function("quadratic_custom", lambda x: 2 * x ** 2 - 3 * x + 1, "f(x) = 2x² - 3x + 1",
                                 "Custom Quadratic"),
    "cubic": Function("cubic", lambda x: x ** 3, "f(x) = x³", "Cubic"),
    "cube_root": Function("cube_root", lambda x: np.cbrt(x), "f(x) = ³√x", "Cube Root"),
    "reciprocal": Function("reciprocal", lambda x: np.where(x != 0, 1 / x, np.nan), "f(x) = 1/x", "Reciprocal"),
    "reciprocal_squared": Function("reciprocal_squared", lambda x: np.where(x != 0, 1 / x ** 2, np.nan),
                                   "f(x) = 1/x²", "Reciprocal Squared")
}

def __str__(self):
    return f"Function: {self.label}\nDescription: {self.description}"



# Example Function Objects
absolute_value = Function("absolute_value", lambda x: np.abs(x), "f(x) = |x|", "Absolute Value")
quadratic_custom = Function("quadratic_custom", lambda x: 2 * x ** 2 - 3 * x + 1, "f(x) = 2x² - 3x + 1",
                            "Custom Quadratic")



# Correct Calls to Scatter Plot
absolute_value.scatter_plot()  # No arguments required; x_range and num_points are optional
quadratic_custom.scatter_plot()


# Optional: A helper function to fetch a specific function by name
def get_function_by_name(name):
    return functions.get(name)


if __name__ == "__main__":
    # Example usage in the same file for testing purposes
    func = get_function_by_name("quadratic")
    if func:
        print(f"Function '{func.name}': {func.description}")
        values = np.array([1, 2, 3, 4])
        print(f"Input: {values}")
        print(f"Output: {func(values)}")
