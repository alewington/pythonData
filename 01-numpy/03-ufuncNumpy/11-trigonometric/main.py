# Trigonometric Functions in NumPy

# Trigonometric functions are mathematical functions that relate the angles of
# a triangle to the lengths of its sides. In NumPy, you can use various
# trigonometric functions to perform calculations on arrays of angles.

import numpy as np

# Create a 1-dimensional array with angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# Calculate the sine of the angles
sine_values = np.sin(angles)
print("Sine Values:", sine_values)
# Calculate the cosine of the angles
cosine_values = np.cos(angles)
print("Cosine Values:", cosine_values)
# Calculate the tangent of the angles
tangent_values = np.tan(angles)
print("Tangent Values:", tangent_values)

# You can also use the shorthand methods for trigonometric functions
sine_values_shorthand = np.sin(angles)
cosine_values_shorthand = np.cos(angles)
tangent_values_shorthand = np.tan(angles)
print("Sine Values (shorthand):", sine_values_shorthand)
print("Cosine Values (shorthand):", cosine_values_shorthand)
print("Tangent Values (shorthand):", tangent_values_shorthand)

# These operations are performed element-wise, meaning that each element in
# the array is transformed according to the specified trigonometric function.
