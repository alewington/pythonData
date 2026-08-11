# Creating arrays in numpy

# Numpy provides a powerful array object called ndarray, which is used to
# represent
# multi-dimensional arrays. You can create an ndarray using the numpy.array()
# function.

import numpy as np

# Create a 1D array
array_1d: np.ndarray = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Create a 2D array
array_2d: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

# Create a 3D array
array_3d: np.ndarray = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(array_3d)

# long arrays with specific values can be created in several ways, for example
# using the arange() function, which creates an array with evenly spaced
# values within a given range.
# for specific values, you can just list them as follows:

array_unique: np.ndarray = np.array([10,
                                    20,
                                    30,
                                    40,
                                    50,
                                    51,
                                    52,
                                    53,
                                    54,
                                    55,
                                    56,
                                    57,
                                    58,
                                    59,
                                    60])

print("\nArray with specific values:")
print(array_unique)

# Other methods will be shown in the next files, but for now, we have created
# a 1D array, a 2D array, and a 3D array using the numpy.array() function.
# You can also create arrays with specific values using the numpy.arange()
# function, which creates an array with evenly spaced values within a given
# range.
