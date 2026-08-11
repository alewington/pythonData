# Iterating Arrays in Numpy

# In NumPy, you can iterate over arrays using various methods. This allows you
# to access and manipulate the elements of an array efficiently.
import numpy as np

# Create a 2D array
array_2d: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Iterate over the rows of the 2D array
print("Iterating over rows:")
for row in array_2d:
    print(row)
# output:
# Iterating over rows:
# [1 2 3]
# [4 5 6]

# Iterate over the columns of the 2D array
print("\nIterating over columns:")
for col in array_2d.T:  # Transpose the array to iterate over columns
    print(col)
# output:
# Iterating over columns:
# [1 4 7]
# [2 5 8]

# Iterate over each element of the 2D array
print("\nIterating over each element:")
for i in range(array_2d.shape[0]):  # Iterate over rows
    for j in range(array_2d.shape[1]):  # Iterate over columns
        print(array_2d[i, j], end=' ')
    print()
# output:
# Iterating over each element:
# 1 2 3
# 4 5 6
# 7 8 9

# Iterate to a straight line array using the `flat` attribute
print("\nIterating over a flattened array:")
for element in array_2d.flat:
    print(element, end=' ')
# output:
# Iterating over a flattened array:
# 1 2 3 4 5 6 7 8 9
