# Area

# The `area` module provides a collection of physical constants related to
# area measurements, including conversion factors between different units of
# area, such as square meters, square feet, and acres. The constants are
# defined using the `scipy.constants` module, which provides a convenient way
# to access these values in a consistent and reliable manner. The module also
# includes functions for converting between different units of area, allowing
# users to easily perform calculations involving area in various units.

# Overall, this module serves as a useful resource for anyone working with
# area measurements in scientific or engineering applications, providing a
# comprehensive set of constants and functions for working with area in a
# variety of contexts.

import scipy.constants as constants

# return in square meters
print("Square foot:", constants.foot**2)  # output: 0.09290304
print("Square inch:", constants.inch**2)  # output: 0.00064516
print("Acre:", constants.acre)  # output: 4046.8564224
print("Hectare:", constants.hectare)  # output: 10000.0
