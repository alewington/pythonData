# Energy

# This module contains physical constants related to energy, such as the
# electron volt, joule, and Planck's constant. These constants are essential
# for calculations in physics and engineering.

import scipy.constants as constants

# return in Joules
print(" to Joules:", constants.eV)
# output: 1.602176634e-19
print("Electron volt:", constants.electron_volt)
# output: 1.602176634e-19
print("Planck's constant:", constants.h)
# output: 6.62607015e-34
print("calorie:", constants.calorie)
# output: 4.184
print("British thermal unit:", constants.Btu)
# output: 1055.05585262
print("BTU international table:", constants.Btu_IT)
# output: 1055.05585262
print("BTU thermochemical:", constants.Btu_th)
# output: 1054.3502644888888
print("Rydberg constant times hc:", constants.Rydberg)
# output: 10973731.568160
print("tonne of TNT:", constants.ton_TNT)
# output: 4184000000.0
