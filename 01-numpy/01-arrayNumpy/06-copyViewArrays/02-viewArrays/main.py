# View Arrays in NumPy

# In NumPy, you can create a view of an array using the `view()` method. This
# creates a new array that shares the same data as the original array but is
# stored in a different memory location. Changes made to the view will affect
# the original array, and vice versa.

import numpy as np

# Create an array
original_array = np.array([1, 2, 3, 4, 5])
# Create a view of the array
view_array = original_array.view()

# Modify the view array
view_array[0] = 10

# Output the original and view arrays to see the difference
print("Original array:", original_array)
print("View array:", view_array)

# output:
# Original array: [10  2  3  4  5]
# View array: [10  2  3  4  5]

# This is an example of how to create a view of an array in NumPy. The
# original array is affected when the view array is modified. This is useful
# when you want to create a new array that shares the same data as the original
# array and you want to make changes to the new array that will also affect the
# original array.

# This is good for updating data in place without creating a
# new copy of the data, which can save memory and improve performance when
# working with large datasets.
