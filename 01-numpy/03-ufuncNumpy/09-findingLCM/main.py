# Finding the Least Common Multiple (LCM) in NumPy

# What is the Least Common Multiple (LCM)?
# The Least Common Multiple (LCM) of two integers is the smallest positive
# integer that is divisible by both of the given integers.
# For example, the LCM of 4 and 6 is 12.

import numpy as np

# Create two 1-dimensional arrays
arr1 = np.array([4, 6, 8])
arr2 = np.array([6, 9, 12])
# Calculate the LCM of the two arrays element-wise
lcm_result = np.lcm(arr1, arr2)
print("LCM of the two arrays:", lcm_result)
# Output: LCM of the two arrays: [12 18 24]

# LCM is a fundamental concept in mathematics and is widely used in various
# fields, including number theory, algebra, and problem-solving. In NumPy,
# the `np.lcm()` function allows you to efficiently compute the LCM of two
# arrays element-wise. This operation is performed element-wise and can handle
# arrays of different shapes through broadcasting.

# In NumPy, the `np.lcm()` function allows you to compute the Least Common
# Multiple (LCM) of two arrays efficiently. It can be used to calculate the
# LCM of corresponding elements in two 1-dimensional arrays or along a specific
# axis in multi-dimensional arrays. This is particularly useful in various
# applications, such as finding common denominators, solving equations, or
# analysing periodic phenomena in scientific and engineering computations.
