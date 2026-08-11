# Data Distribution

# In this example, we will explore how to generate random data using NumPy.
from numpy import random

data_dist = random.choice([1, 3, 5, 7, 9],
                          p=[0.1, 0.3, 0.5, 0.1, 0.0], size=(100))

print(data_dist)

# What does this code do?
# This code generates a random sample of 100 elements from the
# list [1, 3, 5, 7, 9] using the `numpy.random.choice` function.
# The `p` parameter specifies the probabilities associated with each element
# in the list, meaning that:
# - The number 1 has a 10% chance of being selected.
# - The number 3 has a 30% chance of being selected.
# - The number 5 has a 50% chance of being selected.
# - The number 7 has a 10% chance of being selected.
# - The number 9 has a 0% chance of being selected.

# 2-dimensional array
data_dist_2d = random.choice([1, 3, 5, 7, 9],
                             p=[0.1, 0.3, 0.3, 0.1, 0.2], size=(3, 5))

print(data_dist_2d)

# What does this code do?
# This code generates a 2-dimensional array of shape (3, 5) with random
# elements selected from the list [1, 3, 5, 7, 9] using the same probabilities
# as before. Each row of the array will contain 5 elements, and there will be
# 3 rows in total. The selection of elements is still based on the specified
# probabilities, meaning that the distribution of numbers in the 2D array will
# reflect the same likelihoods as in the 1D case.
