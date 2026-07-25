# Join arrays in Numpy

# In NumPy, you can join or concatenate arrays using various functions. This
# allows you to combine multiple arrays into a single array efficiently.

import numpy as np

# Create two 1D arrays
array1: np.ndarray = np.array([1, 2, 3])
array2: np.ndarray = np.array([4, 5, 6])

# Join the two arrays using `np.concatenate()`
joined_array: np.ndarray = np.concatenate((array1, array2))
print(joined_array)

# output:
# [1 2 3 4 5 6]

# What this does?
# The `np.concatenate()` function allows you to join two or more arrays along
# an existing axis. In this example, we joined two 1D arrays into a single
# 1D array. The original arrays remain unchanged.


# join as [[1, 4], [2, 5], [3, 6]]
joined_array2: np.ndarray = np.column_stack((array1, array2))
print(joined_array2)
# output:
# [[1 4]
#  [2 5]
#  [3 6]]

# What this code does?
# The `np.column_stack()` function allows you to join two or more 1D arrays
# as columns into a 2D array. In this example, we joined two 1D arrays into a
# single 2D array with each array as a column. The original arrays remain
# unchanged.
