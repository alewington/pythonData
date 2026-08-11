# Rounding Decimals using NumPy Universal Functions (ufuncs)

# NumPy provides a set of universal functions (ufuncs) that allow you to
# perform element-wise operations on arrays. These functions are optimised
# for performance and can handle broadcasting, which allows you to perform
# operations on arrays of different shapes.

import numpy as np

# Create a 1-dimensional array with decimal values
arr = np.array([1.2345, 2.3456, 3.4567, 4.5678, 5.6789])

# Round the elements of the array to 2 decimal places using ufunc
rounded_arr = np.round(arr, 2)

print("Original Array:", arr)
print("Rounded Array (2 decimal places):", rounded_arr)

# You can also use the shorthand method for rounding
rounded_arr_shorthand = np.around(arr, 2)
print("Rounded Array (shorthand, 2 decimal places):", rounded_arr_shorthand)

# These operations are performed element-wise, meaning that each element in
# the array is rounded to the specified number of decimal places. If the array
# has different shapes, NumPy will attempt to broadcast them to a common shape
# before performing the operation.

# You can also round to different decimal places by changing the second
# argument
rounded_arr_1_decimal = np.round(arr, 1)
print("Rounded Array (1 decimal place):", rounded_arr_1_decimal)

# You can also round to the nearest integer by using 0 as the second argument
rounded_arr_nearest_int = np.round(arr, 0)
print("Rounded Array (nearest integer):", rounded_arr_nearest_int)

# Note: The rounding behavior follows the "round half to even" strategy, also
# known as "bankers' rounding". This means that if the number is exactly
# halfway between two integers, it will round to the nearest even integer.
# example: 2.5 will round to 2, while 3.5 will round to 4.
rounded_half_even = np.round(np.array([2.5, 3.5, 4.5, 5.5]), 0)
print("Rounded Half to Even:", rounded_half_even)

# how not to envoque bankers rounding
# If you want to avoid the "round half to even" behavior and always round
# .5 values up, you can use the np.ceil() function after adding 0.5 to the
# array. This will effectively round .5 values up to the next integer.
rounded_half_up = np.ceil(arr + 0.5)
print("Rounded Half Up:", rounded_half_up)

# You can also use the np.floor() function to round down to the nearest integer
rounded_down = np.floor(arr)
print("Rounded Down:", rounded_down)

# You can also use the np.trunc() function to truncate the decimal part and
# keep only the integer part
truncated_arr = np.trunc(arr)
print("Truncated Array:", truncated_arr)

# In summary, NumPy provides various ufuncs for rounding decimals,
# including:
# - np.round()
# - np.around()
# - np.ceil()
# - np.floor()
# - np.trunc()

# Each of these functions allows you to perform element-wise rounding
# operations on arrays, and you can specify the number of decimal places
# to round to.
