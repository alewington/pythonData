# SciPy Constants

# The `scipy.constants` module provides a collection of physical and
# mathematical constants. These constants are useful in scientific
# calculations and simulations.

from scipy import constants

# Example usage:
print("Speed of light:", constants.c)
print("Gravitational constant:", constants.G)

# The `scipy.constants` module includes a wide range of constants, such as
# fundamental physical constants, mathematical constants, and unit conversions.

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

# The `scipy.constants` module also provides a variety of physical constants,
# such as the speed of light, Planck's constant, and the gravitational
# constant. These constants are essential for scientific calculations and
# simulations in various fields, including physics, chemistry, and engineering.

# they allow you to convert between different units of measurement, such as
# length, mass, time, and more. For example:
print("1 meter in centimeters:", 1 * constants.centi)
print("1 kilogram in grams:", 1 * constants.kilo)

# The `scipy.constants` module also includes a variety of time-related
# constants, such as the number of seconds in a minute, hour, day, and year.
# These constants can be useful for time conversions and calculations in
# various applications. For example:
print("1 minute in seconds:", 1 * constants.minute)
print("1 hour in seconds:", 1 * constants.hour)

# Computer Storage Units (sci units base 10):
print("1 kilobyte in bytes:", 1 * constants.kilo)
print("1 megabyte in bytes:", 1 * constants.mega)
print("1 gigabyte in bytes:", 1 * constants.giga)

# Computer Storage Units (binary units in IEEE 1541 standard base 2):
print("1 kibibyte in bytes:", 1 * constants.kibi)
print("1 mebibyte in bytes:", 1 * constants.mebi)
print("1 gibibyte in bytes:", 1 * constants.gibi)

# CPU Speed Units (sci units):
print("1 kilohertz in hertz:", 1 * constants.kilo)
print("1 megahertz in hertz:", 1 * constants.mega)
print("1 gigahertz in hertz:", 1 * constants.giga)

# teraflops (TFLOPS) is a measure of a computer's performance, especially in
# fields of scientific calculations that require floating-point calculations.
# It represents one trillion (10^12) floating-point operations per second.
print("1 teraflop in FLOPS:", 1 * constants.tera)

# speed in sci units:
print("1 kilometer per hour in meters per second:", 1 * constants.kilo /
      constants.hour)
print("1 mile per hour in meters per second:", 1 * constants.mile /
      constants.hour)
print("1 knot in meters per second:", 1 * constants.knot)

# measurements in sci units:
print("1 inch in meters:", 1 * constants.inch)
print("1 cm in millimeters:", 1 * constants.centi * constants.milli)
