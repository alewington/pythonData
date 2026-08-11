# numpy

# numpy is a powerful library for numerical computing in Python. It provides
# support for large, multi-dimensional arrays and matrices, along with a
# collection of mathematical functions to operate on these arrays.

# It can be up to 50 times faster than traditional Python lists for numerical
# operations, making it a popular choice for data scientists and researchers.
# It is widely used in data analysis, scientific computing, and machine
# learning due to its efficiency and ease of use.

# Partially taken from https://numpy.org/doc/stable/user/whatisnumpy.html

# Website: https://numpy.org
# Documentation: https://numpy.org/doc
# github: https://github.com/numpy/numpy

# To install numpy, you can use either conda or pip. Here are the commands for
# both:

# Using conda:
# conda install numpy

# Using pip:
# pip install numpy

# You can also update numpy using the following commands:

# Using conda:
# conda update numpy

# Using pip:
# pip install --upgrade numpy

# To check if numpy is installed and to see its version, you can run the
# following command in your Python environment:
# python -c "import numpy; print(numpy.__version__)"

# example usage of numpy:
import numpy as np

# Creating a 1-dimensional array
array_1d = np.array([1, 2, 3, 4, 5])
# Creating a 2-dimensional array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Creating an array of zeros
array_zeros = np.zeros((3, 3))

print("1D Array:", array_1d)
print("2D Array:", array_2d)
print("Array of Zeros:\n", array_zeros)
