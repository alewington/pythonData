# SciPy Constants

# The `scipy.constants` module provides a collection of physical and
# mathematical constants. These constants are useful in scientific
# calculations and simulations.

from scipy import constants

# So you are basically able to convert between sci units and non-sci units.
# So metric, IEEE, Imperial and more types of units.

# You can also change the scale of the units from Kilo to Giga for example.

# It is just a case of matching the units and the scale where needed and using
# suitable calculations to get the needed outcome.

# You can apply Optimisers, sparse data, Graphs, Spatial data Matlab,
# interpolation and significance tests.


# lets look at sci units:
# biggest to smallest
print(constants.yotta)  # 1e24
print(constants.zetta)  # 1e21
print(constants.exa)    # 1e18
print(constants.peta)   # 1e15
print(constants.tera)   # 1e12
print(constants.giga)   # 1e9
print(constants.mega)   # 1e6
print(constants.kilo)   # 1e3
print(constants.hecto)  # 1e2
print(constants.deka)   # 1e1
print(constants.deci)   # 1e-1
print(constants.centi)  # 1e-2
print(constants.milli)  # 1e-3
print(constants.micro)  # 1e-6
print(constants.nano)   # 1e-9
print(constants.pico)   # 1e-12
print(constants.femto)  # 1e-15
print(constants.atto)   # 1e-18

# Think of them as 1 unit of something until you get to the next unit.
