import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n_values = np.linspace(2, 1000, 1000)  # Range of n

# Define the complexities
o_1 = np.ones_like(n_values)  # O(1)
o_n = n_values  # O(n)
o_log_n = np.log(n_values)  # O(log n)
o_n_log_n = n_values * np.log(n_values)  # O(n log n)
o_n_squared = n_values**2  # O(n^2)

# Plot the complexities
plt.figure(figsize=(12, 8))

plt.plot(n_values, o_1, label='O(1)', color='green')
plt.plot(n_values, o_n, label='O(n)', color='blue')
plt.plot(n_values, o_log_n, label='O(log n)', color='orange')
plt.plot(n_values, o_n_log_n, label='O(n (log n))', color='purple')
plt.plot(n_values, o_n_squared, label='O(n^2)', color='red')

# Add titles and labels
plt.title("Complexity Comparison for Various Time Complexities", fontsize=16)
plt.xlabel("n (Input Size)", fontsize=14)
plt.ylabel("Complexity", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.yscale('log')  # Use a logarithmic scale for better visualization
plt.show()
