# Creating Universal Functions (ufunc) Example

# You can create your own ufuncs using the np.frompyfunc function.
# This allows you to define a Python function and convert it into a ufunc
# that can operate element-wise on ndarrays.

import numpy as np


# Define a simple Python function that adds two numbers
def add_numbers(x: float | int, y: float | int) -> float | int:
    """Add two numbers.
    Args:
        x (int or float): The first number.
        y (int or float): The second number.
    Returns:
        int or float: The sum of the two numbers.
    Example:
        >>> add_numbers(2, 3)
        5
    """
    return x + y


# Convert the Python function into a ufunc using np.frompyfunc
add_ufunc = np.frompyfunc(add_numbers, 2, 1)

# Example usage of the created ufunc
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = add_ufunc(a, b)

print("Element-wise Addition using ufunc:", result)
# Output: Element-wise Addition using ufunc: [5 7 9]

# What does this code do?
# This code defines a simple Python function called add_numbers that takes two
# arguments and returns their sum. It then uses np.frompyfunc to convert this
# function into a ufunc called add_ufunc. The add_ufunc can be
# applied element-wise to NumPy arrays, allowing for efficient addition of
# corresponding elements in the input arrays. The example demonstrates how to
# use the created ufunc to add two 1-dimensional arrays element-wise,
# resulting in a new array containing the sums of the corresponding elements.

# frompyfunc is a powerful feature of NumPy that allows you to create custom
# ufuncs from regular Python functions. This can be useful when you want to
# apply a specific operation to each element of an array, especially when the
# operation is not available as a built-in ufunc in NumPy. However, keep in
# mind that ufuncs created with frompyfunc may not be as fast as built-in
# ufuncs, especially for large arrays, since they involve Python function
# calls.
