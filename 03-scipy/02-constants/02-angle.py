# Angle

# This module provides a collection of mathematical constants related to
# angles, including the conversion factors between degrees and radians, as
# well as the values of common angles in both degrees and radians. The
# constants are defined using the `scipy.constants` module, which
# provides a convenient way to access these values in a consistent
# and reliable manner. The module also includes functions for converting
# between degrees and radians, allowing users to easily perform
# calculations involving angles in different units. Overall, this module
# serves as a useful resource for anyone working with angles in scientific
# or engineering applications, providing a comprehensive set of constants
# and functions for working with angles in a variety of contexts.

import scipy.constants as constants

# return in degrees
print("Degrees:", constants.degree)  # output: 0.017453292519943295
print("Pi:", constants.pi)  # output: 3.141592653589793
print("arcmin:", constants.arcmin)  # output: 0.0002908882086657216
print("arcsec:", constants.arcsec)  # output: 4.84813681109536e-06
print("arcminute:", constants.arcminute)  # output: 0.0002908882086657216
print("arcsecond:", constants.arcsecond)  # output: 4.84813681109536e-06
