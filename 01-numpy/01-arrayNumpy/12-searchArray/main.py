# Search arrays in Numpy

# In NumPy, you can search for specific elements in an array using various
# functions. This allows you to find the indices of elements that meet certain
# conditions efficiently.

import numpy as np

# Create a 1D array
original_array = np.array([10, 20, 30, 40, 50, 60])

# Search for the index of a specific element using `np.where()`
index = np.where(original_array == 40)
print(index)

# output:
# (array([3]),)

# What this does?
# The `np.where()` function allows you to find the indices of elements that
# meet a specific condition. In this example, we searched for the index of the
# element `40` in the 1D array. The original array remains unchanged.

# Other examples

# Search for elements greater than 30
indices = np.where(original_array > 30)
print(indices)

# output:
# (array([3, 4, 5]),)

# what this does?
# The `np.where()` function allows you to find the indices (index) of
# elements that meet a specific condition. In this example, we searched
# for the indices of elements greater than `30` in the 1D array. The original
# array remains unchanged.

# Using the values from indices
values = original_array[indices]
# this is a filtering operation using the indices obtained from the search
print(values)

# output:
# [40 50 60]

# what this does?
# The `np.where()` function allows you to find the indices (index) of elements
# that meet a specific condition. In this example, we searched for the indices
# of elements greater than `30` in the 1D array and then used those indices to
# filter/retrieve the corresponding values from the original array. The
# original array remains unchanged.
