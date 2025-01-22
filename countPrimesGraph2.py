import timeit
import numpy as np
import matplotlib.pyplot as plt
import time
import math


class Solution(object):
    def countPrimes(self, n):
        """
        Calculate the most significant digit of n!.
        """
        if n < 2:
            return 1  # For n=0 or n=1, factorial is 1.

        # Use logarithms to compute the significant part of the factorial.
        log_sum = 0
        for i in range(1, n + 1):
            log_sum += math.log10(i)

        # Extract the most significant digit from log_sum
        fractional_part = log_sum - int(log_sum)  # Get the fractional part
        significant_digit = int(10 ** fractional_part)  # Convert fractional part to a number

        return significant_digit


# Generate test input sizes
input_sizes = range(1, 300, 100)  # Input sizes from 1 to 5000 incremented by 100
execution_times = []


def measure_execution_time(n, solution):
    """
    Measure the average execution time of countPrimes function over 5 runs.

    :param n: Input size for countPrimes function.
    :param solution: Instance of the Solution class containing countPrimes.
    :return: Average execution time in seconds.
    """
    execution_timer = timeit.Timer(lambda: solution.countPrimes(n))
    warmup_runs = 3  # Warm-up runs to stabilize performance
    for _ in range(warmup_runs):
        execution_timer.timeit(number=1)
    return execution_timer.timeit(number=5) / 5  # Average over 5 runs


def plot_actual_vs_theoretical():
    # Measure execution time for each input size
    solution = Solution()
    for n in input_sizes:
        execution_times.append(measure_execution_time(n, solution))

    # Theoretical complexities
    n_values = np.array(input_sizes)
    o_1 = np.ones_like(n_values)  # O(1)
    o_n = n_values  # O(n)
    o_log_n = np.log(n_values + 1)  # O(log n) (+1 to avoid log(0))
    o_n_log_n = n_values * np.log(n_values + 1)  # O(n log n)
    o_n_squared = n_values ** 2  # O(n^2)
    o_n_log_log_n = n_values * np.log(np.log(n_values + 2))

    # Scaling
    scale_factor_o_1 = min(execution_times)  # Start O(1) from the smallest execution time
    o_1 = o_1 * scale_factor_o_1

    scale_factor_o_n = execution_times[len(execution_times) // 2] / o_n[len(execution_times) // 2]
    o_n = o_n * scale_factor_o_n

    scale_factor_o_log_n = execution_times[len(execution_times) // 2] / o_log_n[len(execution_times) // 2]
    o_log_n = o_log_n * scale_factor_o_log_n

    scale_factor_o_n_log_n = execution_times[len(execution_times) // 2] / o_n_log_n[len(execution_times) // 2]
    o_n_log_n = o_n_log_n * scale_factor_o_n_log_n

    scale_factor_o_n_squared = execution_times[len(execution_times) // 2] / o_n_squared[len(execution_times) // 2]
    o_n_squared = o_n_squared * scale_factor_o_n_squared

    # Plot the complexities and actual execution time
    plt.figure(figsize=(14, 10))
    plt.plot(n_values, o_1, label='O(1)', color='green')
    plt.plot(n_values, o_n, label='O(n)', color='blue')
    plt.plot(n_values, o_log_n, label='O(log n)', color='orange')
    plt.plot(n_values, o_n_log_n, label='O(n log n)', color='purple')
    plt.plot(n_values, o_n_squared, label='O(n^2)', color='red')
    plt.plot(input_sizes, execution_times, label='Actual Execution Time - countPrimes', color='cyan', linestyle='--',
             marker='o', linewidth=2)

    # Add annotations at the end of each line
    plt.text(n_values[-1] * 0.95, o_1[-1], 'O(1)', color='green', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n[-1], 'O(n)', color='blue', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_log_n[-1], 'O(log n)', color='orange', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n_log_n[-1], 'O(n log n)', color='purple', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n_squared[-1], 'O(n^2)', color='red', fontsize=12, ha='left')
    plt.text(input_sizes[-1] * 0.95, execution_times[-1], 'Actual Execution Time', color='cyan', fontsize=10, ha='left')

    # Customize plot
    plt.title("Efficiency Analysis: Actual vs Theoretical Complexities", fontsize=16)
    plt.xlabel("Input Size (n)", fontsize=14)
    plt.ylabel("Time (seconds)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.yscale('log')  # Use logarithmic scale for better visualization
    plt.gca().set_facecolor("white")  # Set background to white
    plt.tight_layout()  # Adjust layout to fit labels and annotations

    # Set y-axis limits
    plt.ylim(min(execution_times) / 10, max(execution_times) * 10)
    plt.show()


# Test and plot
if __name__ == "__main__":
    plot_actual_vs_theoretical()
