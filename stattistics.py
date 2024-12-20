import statistics
import math

data = [1.3, 2.6, 6.7, -0.87, -9.6, 6.3, -8.4]

# Calculate the mean (average)
avg = statistics.mean(data)
print("Mean (Average) =", avg)

# Calculate the median (middle value)
median = statistics.median(data)
print("Median =", median)

# Calculate the mode (most common value)
try:
    mode = statistics.mode(data)
    print("Mode =", mode)
except statistics.StatisticsError:
    print("Mode = No unique mode found")

# Calculate the standard deviation (measure of spread of data)
stdev = statistics.stdev(data)
print("Standard Deviation =", stdev)

# Calculate the variance (average squared deviation from the mean)
variance = statistics.variance(data)
print("Variance =", variance)

# Harmonic Mean (filter out negative values)
positive_data = [x for x in data if x > 0]
try:
    harmonic_mean = statistics.harmonic_mean(positive_data)
    print("Harmonic Mean (only positive values) =", harmonic_mean)
except statistics.StatisticsError as e:
    print("Harmonic Mean = Cannot be calculated due to:", e)

# Geometric Mean (only on positive values)
try:
    geometric_mean = statistics.geometric_mean([abs(x) for x in data if x > 0])
    print("Geometric Mean =", geometric_mean)
except statistics.StatisticsError:
    print("Geometric Mean = Unable to calculate due to negative values")

# Finding the minimum and maximum
min_value = min(data)
max_value = max(data)
print("Minimum =", min_value)
print("Maximum =", max_value)

# Range (difference between max and min)
range_value = max_value - min_value
print("Range =", range_value)
