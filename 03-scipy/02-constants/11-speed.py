# Speed

import scipy.constants as constants

# The `speed` module provides a collection of physical constants related to
# speed measurements, including conversion factors between different units of
# speed, such as meters per second, kilometers per hour, and miles per hour.
# The constants are defined using the `scipy.constants` module, which provides
# a convenient way to access these values in a consistent and reliable manner.

# Overall, this module serves as a useful resource for anyone working with
# speed measurements in scientific or engineering applications, providing a
# comprehensive set of constants and functions for working with speed in a
# variety of contexts.

# return in meters per second
print("KMH", constants.kmh)  # output: 0.2777777777777778
print("MPH", constants.mph)  # output: 0.44703999999999996
print("Knot", constants.knot)  # output: 0.5144444444444445
print("Mach", constants.mach)  # output: 340.5
print("Speed of sound", constants.speed_of_sound)  # output: 340.5
print("Speed of light", constants.c)  # output: 299792458.0
