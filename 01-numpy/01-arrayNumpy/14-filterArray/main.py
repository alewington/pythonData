# Filter an Array in Numpy

# In NumPy, you can filter arrays using boolean indexing. This allows you to
# select elements from an array that meet certain conditions efficiently.
import numpy as np

# Create a 1D array
original_array: np.ndarray = np.array([10, 20, 30, 40, 50, 60])
# Filter elements greater than 30
filtered_array: np.ndarray = original_array[original_array > 30]
print(filtered_array)
# output:
# [40 50 60]

# What this does?
# The boolean indexing allows you to filter elements from an array based on a
# condition. In this example, we filtered the elements of a 1D array that are
# greater than `30`. The original array remains unchanged.

# Difference between filtering and searching?
# Filtering allows you to select elements from an array based on a condition,
# while searching allows you to find the indices of elements that meet a
# specific condition. Filtering returns the actual values that meet the
# condition, while searching returns the indices of those values in the
# original array. Both techniques are useful for working with arrays in NumPy,
# and they can be combined to achieve more complex data manipulation tasks.

# See SearchArray lesson to see them together.
