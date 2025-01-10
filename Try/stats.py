import numpy as np

data = np.array([2, 4, 6, 8, 10])

mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)
variance = np.var(data)

sin_values = np.sin(data)
cos_values = np.cos(data)

exp_values = np.exp(data)
log_values = np.log(data)
log10_values = np.log10(data)

absolute_values = np.abs(data)
square_root = np.sqrt(data)
power_values = np.power(data, 2)

print("Original Array:", data)
print("\nStatistical Functions:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)

print("\nTrigonometric Functions:")
print("Sine Values:", sin_values)
print("Cosine Values:", cos_values)

print("\nExponential and Logarithmic Functions:")
print("Exponential Values:", exp_values)
print("Natural Logarithm Values:", log_values)
print("Base 10 Logarithm Values:", log10_values)

print("\nOther Mathematical Functions:")
print("Absolute Values:", absolute_values)
print("Square Root Values:", square_root)
print("Squared Values:", power_values)