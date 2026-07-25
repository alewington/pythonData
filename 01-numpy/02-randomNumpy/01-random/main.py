# Random numbers in NumPy
# In NumPy, you can generate random numbers using the `numpy.random` module.
# This module provides various functions to generate random numbers from
# different distributions.

import numpy as np

# Generate a random float between 0 and 1
random_float: float = np.random.rand()
print("Random float between 0 and 1:", random_float)

# Output:
# Random float between 0 and 1: 0.3745401188473625
# The number will be different each time you run the code.

# Generate a random integer between 0 and 10
random_integer: int = np.random.randint(0, 10)
print("Random integer between 0 and 10:", random_integer)

# Output:
# Random integer between 0 and 10: 7
# The number will be different each time you run the code.

# Generate a random array of shape (2, 3) with values between 0 and 1
random_array: np.ndarray = np.random.rand(2, 3)
print("Random array of shape (2, 3):")
print(random_array)

# Output:
# Random array of shape (2, 3):
# [[0.95071431 0.73199394 0.59865848]
#  [0.15601864 0.15599452 0.05808361]]
# The values will be different each time you run the code.

# Generate a random array of integers between 0 and 10 with shape (3, 4)
random_int_array: np.ndarray = np.random.randint(0, 10, size=(3, 4))
print("Random integer array of shape (3, 4):")
print(random_int_array)

# Output:
# Random integer array of shape (3, 4):
# [[3 7 2 5]
#  [4 6 8 1]
#  [0 9 3 2]]
# The values will be different each time you run the code.
