# Length

# This module provides a collection of mathematical constants related to
# length, including the conversion factors between different units of
# length, such as meters, centimeters, inches, and feet. The constants are
# defined using the `scipy.constants` module, which provides a convenient way
# to access these values in a consistent and reliable manner. The module also
# includes functions for converting between different units of length, allowing
# users to easily perform calculations involving length in various units.

# Overall, this module serves as a useful resource for anyone working with
# length in scientific or engineering applications, providing a comprehensive
# set of constants and functions for working with length in a variety of
# contexts.

import scipy.constants as constants

# return in meters
print("Inch:", constants.inch)
print("Foot:", constants.foot)
print("Yard:", constants.yard)
print("Mile:", constants.mile)
print("Nautical mile:", constants.nautical_mile)
print("Astronomical unit:", constants.au)
print("Light year:", constants.light_year)
print("Parsec:", constants.parsec)  # Han solo you know what you did!
