# Universal Functions (ufunc) Example

# Universal functions (ufuncs) are functions that operate element-wise on
# ndarrays. They are highly optimized and provide a fast way to perform
# element-wise operations on large arrays. Examples of ufuncs include
# np.add, np.subtract, np.multiply, np.divide, np.sin, np.cos, np.exp, and
# np.log.

import numpy as np
# Create two 1-dimensional arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
# Perform element-wise addition using ufunc
result_add = np.add(a, b)
# Perform element-wise multiplication using ufunc
result_multiply = np.multiply(a, b)
print("Element-wise Addition:", result_add)
print("Element-wise Multiplication:", result_multiply)

# You probably have seen the use of ufuncs in the previous examples,
# such as:
# - np.random.rayleigh
# - np.random.multivariate_normal
# - np.random.multinomial

# These functions are also ufuncs that operate on arrays to generate random
# samples from specific probability distributions.
