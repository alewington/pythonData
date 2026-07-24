# Slicing

# Slicing is a way to extract a portion of an array. It allows you to select
# specific elements or ranges of elements from an array.
# It is similar to slicing in Python lists, but it can be applied to
# multi-dimensional arrays as well.

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array_1d)  # Output: [ 1  2  3  4  5  6  7  8  9 10]

print("Slicing the array")

print(array_1d[2:5])
# Output: [3 4 5] - elements from index 2 to 4

print(array_1d[:4])
# Output: [1 2 3 4] - elements from the start to index 3

print(array_1d[5:])
# Output: [ 6  7  8  9 10] - elements from index 5 to the end

print(array_1d[::2])
# Output: [1 3 5 7 9] - every second element

print(array_1d[::-1])
# Output: [10  9  8  7  6  5  4  3  2  1] - reverse the array

print(array_1d[1:8:2])
# Output: [2 4 6 8] - elements from index 1 to 7 with a step of 2

print(array_1d[-3:])
# Output: [ 8  9 10] - last three elements

print(array_1d[:-3])
# Output: [1 2 3 4 5 6 7] - all elements except the last three

print(array_1d[-5:-2])
# Output: [6 7 8] - elements from index -5 to -3

print(np.sum(array_1d[3:7]))
# Output: 22 - sum of elements from index 3 to 6 (4 + 5 + 6 + 7)

# Slicing can also be applied to multi-dimensional arrays. For example, in a
# 2D array, you can slice rows and columns.
# You can do a lot with slicing to pull out specific elements, rows, columns,
# or sub-arrays from a multi-dimensional array.
