# Indexing Arrays with NumPy

# In this example, we will demonstrate how to index arrays using NumPy.
# Indexing allows you to access specific elements or slices of an array.

import numpy as np

list_of_nums: np.ndarray = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Accessing elements using positive indices
print("Accessing elements using positive indices:")
print(list_of_nums[0])  # Output: 10 - first element
print(list_of_nums[3])  # Output: 40 - fourth element

# Accessing elements using negative indices
print("\nAccessing elements using negative indices:")
print(list_of_nums[-1])  # Output: 100 - last element
print(list_of_nums[-4])  # Output: 70 - fourth element from the end

# Calculate with indexing
print("\nCalculating with indexing:")
print(list_of_nums[0] + list_of_nums[1])
# Output: 30 - sum of first and second elements
print(list_of_nums[2] * list_of_nums[3])
# Output: 1200 - product of third and fourth elements
