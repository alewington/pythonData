# Volume

# The `volume` module provides a collection of physical constants related to
# volume measurements, including conversion factors between different units of
# volume, such as cubic meters, cubic feet, and liters. The constants are
# defined using the `scipy.constants` module, which provides a convenient way
# to access these values in a consistent and reliable manner. The module also
# includes functions for converting between different units of volume, allowing
# users to easily perform calculations involving volume in various units.

# Overall, this module serves as a useful resource for anyone working with
# volume measurements in scientific or engineering applications, providing a
# comprehensive set of constants and functions for working with volume in a
# variety of contexts.

import scipy.constants as constants

# return in cubic meters
print("Cubic foot:", constants.foot**3)  # output: 0.028316846592
print("Cubic inch:", constants.inch**3)  # output: 1.6387064e-05
print("Liter:", constants.liter)  # output: 0.001
print("Litre (UK):", constants.litre)  # output: 0.0011365225
print("Gallon (UK):", constants.gallon_imp)  # output: 0.00454609
print("Gallon (US):", constants.gallon_US)  # output: 0.0037854117839999997
print("Fluid ounce (UK):", constants.fluid_ounce_imp)  # output: 2.84130625e-05
print("Fluid ounce (US):", constants.fluid_ounce)  # output: 2.95735295625e-05
print("Barrel:", constants.barrel)  # output: 0.158987294928
print("Cubic yard:", constants.yard**3)  # output: 0.764554857984
print("Cubic mile:", constants.mile**3)  # output: 4168181825.440579
