# Force

# This module provides a collection of mathematical constants related to
# force, including the newton, dyne, and pound-force. The constants are
# defined using the `scipy.constants` module, which provides a convenient
# way to access these values in a consistent and reliable manner.

import scipy.constants as constants

# return in Newtons
print("Dyne:", constants.dyne)  # output: 1e-05
print("Pound-force:", constants.lbf)  # output: 4.4482216152605
print("Pound-force:", constants.pound_force)  # output: 4.4482216152605
print("Kilogram-force:", constants.kgf)  # output: 9.80665
print("Kilogram-force:", constants.kilogram_force)  # output: 9.80665
