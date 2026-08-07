# Mass

# The `mass` module provides a collection of physical constants related to
# mass, including the atomic mass unit, the mass of various subatomic
# particles, and the mass of common objects. These constants are essential for
# scientific calculations and simulations in physics, chemistry, and
# engineering.

import scipy.constants as constants

# return the mass of an electron in kilograms
print("Unified atomic mass unit (u):", constants.u)
# output: Unified atomic mass unit (u): 1.66053906660e-27
print("Mass of electron (kg):", constants.m_e)
# output: Mass of electron (kg): 9.1093837015e-31
print("Mass of proton (kg):", constants.m_p)
# output: Mass of proton (kg): 1.67262192369e-27
print("Mass of neutron (kg):", constants.m_n)
# output: Mass of neutron (kg): 1.67492749804e-27
print("Mass of uranium-235 (kg):", constants.m_u)
# output: Mass of uranium-235 (kg): 3.902e-25
print("Mass of carat (ct):", constants.carat)
# output: Mass of carat (ct): 0.0002
print("Mass of pound (lb):", constants.lb)
# output: Mass of pound (lb): 0.45359237
print("Mass of ounce (oz):", constants.oz)
# output: Mass of ounce (oz): 0.028349523125
print("Mass of stone (st):", constants.stone)
# output: Mass of stone (st): 6.35029318
print("Mass of gram (g):", constants.gram)
# output: Mass of gram (g): 0.001
print("Mass of ton (t):", constants.metric_ton)
# output: Mass of ton (t): 1000.0
print("Mass of short ton (ton_us):", constants.short_ton)
# output: Mass of short ton (ton_us): 907.18474
print("Mass of long ton (ton_uk):", constants.long_ton)
# output: Mass of long ton (ton_uk): 1016.0469088

# there are many others to explore in the `scipy.constants` module.
