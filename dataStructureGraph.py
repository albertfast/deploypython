import numpy as np
import statistics
from math import sqrt

# Data
data = {
    "x1": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    "y1": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    "x2": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    "y2": [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    "x3": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    "y3": [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    "x4": [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    "y4": [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
}


# Function to calculate correlation
def calculate_correlation(x, y):
    n = len(x)
    mean_x, mean_y = statistics.mean(x), statistics.mean(y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    stddev_x = sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    stddev_y = sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    # Handle division by zero safely
    if stddev_x == 0 or stddev_y == 0:
        return None  # Correlation is undefined
    return covariance / (stddev_x * stddev_y)


# Calculate results
results = {
    "Set": ["x1, y1", "x2, y2", "x3, y3", "x4, y4"],
    "mean x": [
        statistics.mean(data["x1"]),
        statistics.mean(data["x2"]),
        statistics.mean(data["x3"]),
        statistics.mean(data["x4"])
    ],
    "s.d. x": [
        statistics.stdev(data["x1"]),
        statistics.stdev(data["x2"]),
        statistics.stdev(data["x3"]),
        statistics.stdev(data["x4"])
    ],
    "mean y": [
        statistics.mean(data["y1"]),
        statistics.mean(data["y2"]),
        statistics.mean(data["y3"]),
        statistics.mean(data["y4"])
    ],
    "s.d. y": [
        statistics.stdev(data["y1"]),
        statistics.stdev(data["y2"]),
        statistics.stdev(data["y3"]),
        statistics.stdev(data["y4"])
    ],
    "cor (x,y)": [
        calculate_correlation(data["x1"], data["y1"]),
        calculate_correlation(data["x2"], data["y2"]),
        calculate_correlation(data["x3"], data["y3"]),
        calculate_correlation(data["x4"], data["y4"])
    ]
}

# Print results in readable format
print("\nResults:")
for i in range(len(results["Set"])):
    correlation = results["cor (x,y)"][i]
    correlation_str = f"{correlation:.2f}" if correlation is not None else "undefined"
    print(f"{results['Set'][i]} - mean x: {results['mean x'][i]:.2f}, s.d. x: {results['s.d. x'][i]:.2f}, "
          f"mean y: {results['mean y'][i]:.2f}, s.d. y: {results['s.d. y'][i]:.2f}, cor(x, y): {correlation_str}")
