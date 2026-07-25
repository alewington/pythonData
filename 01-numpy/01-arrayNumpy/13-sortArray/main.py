# Sort an Array in Numpy

# In NumPy, you can sort arrays using the `np.sort()` function. This allows you
# to arrange the elements of an array in ascending order efficiently.

import numpy as np

# Create a 1D array
original_array: np.ndarray = np.array([5, 2, 9, 1, 5, 6])
print("Original array:", original_array)
# output:
# Original array: [5 2 9 1 5 6]

# Sort the array in ascending order
sorted_array: np.ndarray = np.sort(original_array)
print(sorted_array)
# output:
# [1 2 5 5 6 9]

# What this does?
# The `np.sort()` function allows you to sort the elements of an array in
# ascending order without modifying the original data. In this example, we
# sorted a 1D array with 6 elements. The original array remains unchanged.
