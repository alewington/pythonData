# Randon Permutation

# Random permutation of a sequence, or return a permuted range.
# Permute a sequence, or return a permuted range.
# The random permutation of a sequence is a rearrangement of its elements into
# a random order.

from numpy import arange, random

# Example: Random permutation of a 1D array
made_range = arange(1, 100, 10)
print("Original array:", made_range)
# output: Original array: [ 1 11 21 31 41 51 61 71 81 91]

permuted_array = random.permutation(made_range)
print("Permuted array:", permuted_array)
# output: Permuted array: [ 1 11 21 31 41 51 61 71 81 91]


# Example: Random permutation of a 2D array
two_d_array = random.randint(1, 100, size=(3, 4))
print("Original 2D array:\n", two_d_array)
# output: Original 2D array:
# [[ 1 11 21 31]
#  [41 51 61 71]
#  [81 91  1 11]]

permuted_2d_array = random.permutation(two_d_array)
print("Permuted 2D array:\n", permuted_2d_array)
# output: Permuted 2D array:
# [[ 1 11 21 31]
#  [41 51 61 71]
#  [81 91  1 11]]

# What does permutation do?

# The `random.permutation` function in NumPy generates a random permutation of
# a sequence or array. It rearranges the elements of the input array into
# a new order, which is randomly determined.
