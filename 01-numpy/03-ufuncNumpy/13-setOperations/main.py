# Set Operations in NumPy

# Set operations are a fundamental concept in mathematics and computer science.
# In NumPy, you can perform set operations on arrays using various functions.
# These operations allow you to find common elements, unique elements, and
# differences between arrays.

import numpy as np

# Create two 1-dimensional arrays with some overlapping values
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

# Calculate the union of the two arrays
union_result = np.union1d(array1, array2)
print("Union of array1 and array2:", union_result)

# Calculate the intersection of the two arrays
intersection_result = np.intersect1d(array1, array2)
print("Intersection of array1 and array2:", intersection_result)
# Calculate the difference of the two arrays (elements in array1 not in array2)
difference_result = np.setdiff1d(array1, array2)
print("Difference of array1 and array2 (array1 - array2):", difference_result)

# Calculate the symmetric difference of the two arrays (elements in either
# array1 or array2 but not both)
symmetric_difference_result = np.setxor1d(array1, array2)
print("Symmetric Difference of array1 and array2:",
      symmetric_difference_result)

# These set operations are useful in various applications, such as data
# analysis, where you may need to find common or unique elements between
# datasets, or in mathematical problems that involve set theory.
