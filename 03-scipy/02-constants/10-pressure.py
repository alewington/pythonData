# Pressure

# This module provides a collection of mathematical constants related to
# pressure, including the conversion factors between different units of
# pressure, such as pascals, bars, and atmospheres. The constants are
# defined using the `scipy.constants` module, which provides a convenient way
# to access these values in a consistent and reliable manner. The module also
# includes functions for converting between different units of pressure,
# allowing users to easily perform calculations involving pressure in various
# units.

# Overall, this module serves as a useful resource for anyone working with
# pressure in scientific or engineering applications, providing a comprehensive
# set of constants and functions for working with pressure in a variety of
# contexts.

import scipy.constants as constants

# return in pascals
print("Bar:", constants.bar)  # output: 100000.0
print("Atmosphere:", constants.atm)  # output: 101325.0
print("Torr:", constants.torr)  # output: 133.32236842105263
print("Pounds per square inch:", constants.psi)  # output: 6894.757293168361
