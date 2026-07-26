# Hyperbolic Functions in NumPy

# NumPy provides a set of universal functions (ufuncs) that allow you to
# perform element-wise operations on arrays. These functions are optimised
# for performance and can handle broadcasting, which allows you to perform
# operations on arrays of different shapes.

import numpy as np

# Create a 1-dimensional array with values
values = np.array([-2, -1, 0, 1, 2])

# Calculate the hyperbolic sine of the values
sinh_values = np.sinh(values)
print("Hyperbolic Sine Values:", sinh_values)
# Calculate the hyperbolic cosine of the values
cosh_values = np.cosh(values)
print("Hyperbolic Cosine Values:", cosh_values)
# Calculate the hyperbolic tangent of the values
tanh_values = np.tanh(values)
print("Hyperbolic Tangent Values:", tanh_values)

# You can also use the shorthand methods for hyperbolic functions
sinh_values_shorthand = np.sinh(values)
cosh_values_shorthand = np.cosh(values)
tanh_values_shorthand = np.tanh(values)
print("Hyperbolic Sine Values (shorthand):", sinh_values_shorthand)
print("Hyperbolic Cosine Values (shorthand):", cosh_values_shorthand)
print("Hyperbolic Tangent Values (shorthand):", tanh_values_shorthand)

# These operations are performed element-wise, meaning that each element in
# the array is transformed according to the specified hyperbolic function.

# You can also use the inverse hyperbolic functions provided by NumPy.
# For example, you can calculate the inverse hyperbolic sine, cosine, and
# tangent using the `arcsinh`, `arccosh`, and `arctanh` functions,
# respectively.

# These functions are useful in various mathematical and scientific
# applications, such as solving equations involving hyperbolic functions
# or analysing data that exhibits hyperbolic behavior.

# *Hyperbolic functions* are particularly important in fields such as physics,
# engineering, and computer graphics, where they can describe phenomena like
# wave propagation, heat transfer, and hyperbolic geometry.
