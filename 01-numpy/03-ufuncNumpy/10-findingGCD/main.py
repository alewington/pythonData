# Finding the Greatest Common Divisor (GCD) in NumPy

# What is the Greatest Common Divisor (GCD)?
# The Greatest Common Divisor (GCD) of two integers is the largest positive
# integer that divides both of the given integers without leaving a remainder.
# For example, the GCD of 8 and 12 is 4.

import numpy as np

# Create two 1-dimensional arrays
arr1 = np.array([8, 12, 16])
arr2 = np.array([12, 18, 24])
# Calculate the GCD of the two arrays element-wise
gcd_result = np.gcd(arr1, arr2)
print("GCD of the two arrays:", gcd_result)
# Output: GCD of the two arrays: [4 6 8]

# GCD is a fundamental concept in mathematics and is widely used in various
# fields, including number theory, algebra, and problem-solving. In NumPy,
# the `np.gcd()` function allows you to efficiently compute the GCD of two
# arrays element-wise. This operation is performed element-wise and can handle
# arrays of different shapes through broadcasting.

# In NumPy, the `np.gcd()` function allows you to compute the Greatest Common
# Divisor (GCD) of two arrays efficiently. It can be used to calculate the
# GCD of corresponding elements in two 1-dimensional arrays or along a specific
# axis in multi-dimensional arrays. This is particularly useful in various
# applications, such as simplifying fractions, finding common factors, or
# analysing divisibility properties in scientific and engineering computations.
