# Reshape Arrays in NumPy

# In NumPy, you can change the shape of an array using the `reshape()` method.
# This allows you to create a new view of the array with a different shape
# without modifying the original data.

import numpy as np

# Create a 1D array
original_array: np.ndarray = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array to a 2D array with 2 rows and 3 columns
reshaped_array: np.ndarray = original_array.reshape(2, 3)

print(reshaped_array)
# output:
# [[1 2 3]
#  [4 5 6]]

# What this does?
# The `reshape()` method allows you to change the shape of an array without
# modifying the original data. In this example, we reshaped a 1D array with
# 6 elements into a 2D array with 2 rows and 3 columns. The original array
# remains unchanged.

reshaped_array2: np.ndarray = original_array.reshape(3, 2)
print(reshaped_array2)
# output:
# [[1 2]
#  [3 4]
#  [5 6]]

# This time we reshaped the original 1D array into a 2D array with 3 rows and
# 2 columns. The original array remains unchanged.
