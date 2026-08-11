# Copy Arrays in NumPy

# In NumPy, you can create a copy of an array using the `copy()` method.
# This creates a new array that contains the same data as the original array
# but is stored in a different memory location. Changes made to the copy do
# not affect the original array, and vice versa.

import numpy as np

# Create an array
original_array: np.ndarray = np.array([1, 2, 3, 4, 5])

# Create a copy of the array
copied_array: np.ndarray = original_array.copy()

# Modify the copied array
copied_array[0] = 10

# Output the original and copied arrays to see the difference
print("Original array:", original_array)
print("Copied array:", copied_array)

# output:
# Original array: [1 2 3 4 5]
# Copied array: [10  2  3  4  5]

# This is an example of how to create a copy of an array in NumPy.
# The original array remains unchanged when the copied array is modified.
# This useful when you want to create a new array that is independent of the
# original array and you want to make changes to the new array without
# affecting the original array.

# This is good for testing new methods or algorithms on a copy of the data
# while keeping the original data intact for comparison or reference.
