# Summations in NumPy

import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])
# Calculate the sum of all elements in the array
total_sum = np.sum(arr)
print("Total Sum:", total_sum)
# Calculate the sum of elements along a specific axis (if it were a
# multi-dimensional array)

# Summations are fundamental operations in mathematics and are widely used in
# various fields, including statistics, data analysis, and scientific
# computing. In NumPy, the `np.sum()` function allows you to efficiently
# compute the sum of array elements, either for the entire array or along
# a specified axis. This operation is performed element-wise and can handle
# arrays of different shapes through broadcasting.

# Think of it as adding up all the numbers in a list or a matrix.
# For example, if you have a 2-dimensional array (matrix), you can sum the
# elements along a specific axis:

# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# sum_along_axis0 = np.sum(matrix, axis=0)  # Sum along columns
# sum_along_axis1 = np.sum(matrix, axis=1)  # Sum along rows

# This helps in various applications, such as calculating totals, averages, or
# other aggregate measures.

# In summary, summations in NumPy are a powerful tool for efficiently
# aggregating data, and the `np.sum()` function provides a convenient way to
# perform this operation on arrays of any shape, making it a fundamental
# operation in numerical computing and data analysis.
