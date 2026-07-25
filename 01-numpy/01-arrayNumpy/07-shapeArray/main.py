# Shape Arrays in NumPy

# In NumPy, you can change the shape of an array using the `reshape()` method.
# This allows you to create a new view of the array with a different shape
# without modifying the original data.

import numpy as np

# Create a 2D array
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# output the original array shape.
print(original_array.shape)

# What does shape do?
# The shape of an array is a tuple that represents the dimensions of the array.
# It tells you how many elements are in each dimension of the array.

# For example, a 2D array with 2 rows and 3 columns will have a shape of
# (2, 3). The shape can be accessed using the `shape` attribute of the NumPy
# array.
