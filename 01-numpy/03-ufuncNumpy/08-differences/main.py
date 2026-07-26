# Differences in NumPy

# What is a difference?
# A difference is the result of subtracting one number from another. In
# mathematics, the difference between two numbers is obtained by
# subtracting the second number from the first. For example, the difference
# between the numbers 5 and 3 is calculated as follows:
# 5 - 3 = 2

import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])
# Calculate the difference between consecutive elements in the array
differences = np.diff(arr)
print("Differences between consecutive elements:", differences)
# Output: Differences between consecutive elements: [1 1 1 1]

# Differences are fundamental operations in mathematics and are widely used in
# various fields, including statistics, data analysis, and scientific
# computing. In NumPy, the `np.diff()` function allows you to efficiently
# compute the difference between consecutive elements in an array. This
# operation is performed element-wise and can handle arrays of different
# shapes through broadcasting.

# In NumPy, the `np.diff()` function allows you to compute the difference
# of consecutive elements in an array efficiently. It can be used to calculate
# the difference between elements in a 1-dimensional array or along a specific
# axis in a multi-dimensional array. This is particularly useful in various
# applications, such as calculating changes in data, analyzing trends, or
# identifying patterns in numerical values in scientific and engineering
# computations.
