# Scipy

# SciPy is a Python library used for scientific and technical computing. It
# provides a wide range of functions and algorithms for numerical integration,
# optimisation, signal processing, linear algebra, and more. SciPy is built on
# top of NumPy and provides additional functionality for scientific computing.

# example usage of SciPy:
# Example: Using the `scipy.integrate` module for numerical integration
from scipy import integrate
import numpy as np


# Define a function to integrate
def f(x):
    """Compute the sine of a given value.

    Args:
        x (float): The input value in radians.

    Returns:
        float: The sine of the input value.
    outputs:
        >>> f(np.pi / 2)
        1.0
        # The function `f` takes a single argument `x`, which is expected to
        # be a float representing an angle in radians. It returns the sine of
        # the input value using the `np.sin` function from the NumPy library.
        # The output is also a float representing the sine of the input angle.
        # The example usage demonstrates that when the input is π/2 radians
        # (90 degrees), the output is 1.0, which is the expected value for the
        # sine of 90 degrees.

"""
    return np.sin(x)


# Perform numerical integration using the `quad` function
result, error = integrate.quad(f, 0, np.pi)
print("Result of integration:", result)
# output: Result of integration: 2.0

# How we get the answer 2.0 is by integrating the sine function from 0 to π.
# The integral of sin(x) over this interval is equal to 2, which is the area
# under the curve of the sine function between these two points.

# This code is for scientific computing using Python. It includes importing
# necessary libraries and setting up the environment for scientific computing
# tasks. The code is broken into sections for better understanding and
# organisation. Each section will cover different aspects of scientific
# computing, including numerical integration, optimisation, signal processing,
# and linear algebra.
