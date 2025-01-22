import timeit
import numpy as np
import matplotlib.pyplot as plt
import time
import math

class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        index = 2
        while index * index < n:
            if isPrime[index]:
                for multiple in range(index * index, n, index):
                    isPrime[multiple] = False
            index += 1
        return sum(isPrime)

    def count_primes_adapted(self, n):
        # Edge case: if n is less than 2, there are no primes
        if n < 2:
            return 0

        # Step 1: Create a boolean list to track prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Step 2: Apply the Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):  # Only go up to the square root of n
            if is_prime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i):  # Start from i^2 to avoid redundant work
                    is_prime[j] = False

        # Step 3: Count and return the number of primes
        return sum(is_prime)



# Generate test input sizes
input_sizes = range(1, 300, 100)  # Input sizes from 1 to 5000 incremented by 100
execution_times_adapted = []
execution_times_primes = []

def measure_execution_time(n, solution, func_name):
    """
    Measure the average execution time of countPrimes function over 5 runs.

    :param n: Input size for countPrimes function.
    :param solution: Instance of the Solution class containing countPrimes.
    :return: Average execution time in seconds.
    """
    execution_timer = timeit.Timer(lambda: func_name(n))
    warmup_runs = 3  # Warm-up runs to stabilize performance
    for _ in range(warmup_runs):
        execution_timer.timeit(number=1)
    return execution_timer.timeit(number=5) / 5  # Average over 5 runs


def plot_actual_vs_theoretical():
    # Measure execution time for each input size
    solution = Solution()
    for n in input_sizes:
        execution_times_adapted.append(measure_execution_time(n,solution,solution.count_primes_adapted))
        execution_times_primes.append(measure_execution_time(n,solution, solution.countPrimes))


    # Theoretical complexities
    n_values = np.array(input_sizes)
    o_1 = np.ones_like(n_values)  # O(1)
    o_n = n_values  # O(n)
    o_log_n = np.log(n_values + 1)  # O(log n) (+1 to avoid log(0))
    o_n_log_n = n_values * np.log(n_values + 1)  # O(n log n)
    o_n_squared = n_values ** 2  # O(n^2)
    o_n_log_log_n = n_values*np.log(np.log(n_values+2))

    # Ölçeklendirme
    scale_factor_o_1 = min(min(execution_times_primes),min(execution_times_adapted)) # O(1) in başlangıç noktası
    o_1 = o_1 * scale_factor_o_1

    scale_factor_o_n = execution_times_primes[len(execution_times_primes)//2] / o_n[len(execution_times_primes)//2]
    o_n = o_n * scale_factor_o_n

    scale_factor_o_log_n = execution_times_primes[len(execution_times_primes)//2] / o_log_n[len(execution_times_primes)//2]
    o_log_n = o_log_n * scale_factor_o_log_n

    scale_factor_o_n_log_n = execution_times_primes[len(execution_times_primes)//2] / o_n_log_n[len(execution_times_primes)//2]
    o_n_log_n = o_n_log_n * scale_factor_o_n_log_n

    scale_factor_o_n_squared = execution_times_adapted[len(execution_times_adapted)//2] / o_n_squared[len(execution_times_adapted)//2]
    o_n_squared = o_n_squared * scale_factor_o_n_squared


    # Plot the complexities and actual execution time
    plt.figure(figsize=(14, 10))
    plt.plot(n_values, o_1, label='O(1)', color='green')
    plt.plot(n_values, o_n, label='O(n)', color='blue')
    plt.plot(n_values, o_log_n, label='O(log n)', color='orange')
    plt.plot(n_values, o_n_log_n, label='O(n log n)', color='purple')
    plt.plot(n_values, o_n_squared, label='O(n^2)', color='red')
    plt.plot(input_sizes, execution_times_primes, label='Actual Execution Time - countPrimes', color='cyan', linestyle='--', marker='o', linewidth=2)
    plt.plot(input_sizes, execution_times_adapted, label='Actual Execution Time - count_primes_adapted', color='magenta', linestyle='--', marker='x', linewidth=2)

    # Add annotations at the end of each line
    plt.text(n_values[-1] * 0.95, o_1[-1], 'O(1)', color='green', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n[-1], 'O(n)', color='blue', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_log_n[-1], 'O(log n)', color='orange', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n_log_n[-1], 'O(n log n)', color='purple', fontsize=12, ha='left')
    plt.text(n_values[-1] * 0.95, o_n_squared[-1], 'O(n^2)', color='red', fontsize=12, ha='left')
    plt.text(input_sizes[-1] * 0.95, execution_times_primes[-1], 'Actual Execution Time - countPrimes', color='cyan', fontsize=10, ha='left')
    plt.text(input_sizes[-1] * 0.95, execution_times_adapted[-1], 'Actual Execution Time - count_primes_adapted', color='magenta', fontsize=10, ha='left')

    # Customize plot
    plt.title("Efficiency Analysis: Actual vs Theoretical Complexities", fontsize=16)
    plt.xlabel("Input Size (n)", fontsize=14)
    plt.ylabel("Time (seconds)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.yscale('log')  # Use logarithmic scale for better visualization
    plt.gca().set_facecolor("white")  # Set background to white
    plt.tight_layout()  # Adjust layout to fit labels and annotations

        # Y ekseni limitlerini belirle
    plt.ylim(min(min(execution_times_primes),min(execution_times_adapted)) / 10, max(max(execution_times_primes),max(execution_times_adapted)) * 10)
    plt.show()


# Test and plot
if __name__ == "__main__":

    plot_actual_vs_theoretical()