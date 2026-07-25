# Split arrays in Numpy

# In NumPy, you can split arrays into multiple sub-arrays using various
# functions. This allows you to divide an array into smaller parts efficiently.

import numpy as np

# Create a 1D array
original_array: np.ndarray = np.array([1, 2, 3, 4, 5, 6])

# Split the array into 3 equal parts using `np.array_split()`
split_array: list[np.ndarray] = np.array_split(original_array, 3)
print(split_array)
# output:
# [array([1, 2]), array([3, 4]), array([5, 6])]

# What this does?
# The `np.array_split()` function allows you to split an array into multiple
# sub-arrays without modifying the original data. In this example,
# we split a 1D array with 6 elements into 3 equal parts. The original array
# remains unchanged.
