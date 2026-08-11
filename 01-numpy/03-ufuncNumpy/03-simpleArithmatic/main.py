# Simple Arithmetic Operations using NumPy Universal Functions (ufuncs)

# NumPy provides a set of universal functions (ufuncs) that allow you to
# perform element-wise operations on arrays. These functions are optimized
# for performance and can handle broadcasting, which allows you to perform
# operations on arrays of different shapes.

import numpy as np

# Create two 1-dimensional arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Perform element-wise addition using ufunc
result_add = np.add(a, b)
# Perform element-wise subtraction using ufunc
result_subtract = np.subtract(a, b)
# Perform element-wise multiplication using ufunc
result_multiply = np.multiply(a, b)
# Perform element-wise division using ufunc
result_divide = np.divide(a, b)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)

# You can also use the shorthand operators for these operations:
result_add_shorthand = a + b
result_subtract_shorthand = a - b
result_multiply_shorthand = a * b
result_divide_shorthand = a / b

print("Addition (shorthand):", result_add_shorthand)
print("Subtraction (shorthand):", result_subtract_shorthand)
print("Multiplication (shorthand):", result_multiply_shorthand)
print("Division (shorthand):", result_divide_shorthand)

# These operations are performed element-wise, meaning that each element in
# the first array is combined with the corresponding element in the
# second array. If the arrays have different shapes, NumPy will attempt to
# broadcast them to a common shape before performing the operation.
