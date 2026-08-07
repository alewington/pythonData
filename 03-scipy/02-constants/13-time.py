# Time

# This module provides a collection of mathematical constants related to
# time, including the number of seconds in a minute, hour, day, and year.
# The constants are defined using the `scipy.constants` module, which
# provides a convenient way to access these values in a consistent
# and reliable manner. The module also includes functions for converting
# between different units of time, allowing users to easily perform
# calculations involving time in various units.

import scipy.constants as constants

# return in seconds
print("Minute:", constants.minute)  # output: 60.0
print("Hour:", constants.hour)  # output: 3600.0
print("Day:", constants.day)  # output: 86400.0
print("Week:", constants.week)  # output: 604800.0
print("Year:", constants.year)  # output: 31536000.0
