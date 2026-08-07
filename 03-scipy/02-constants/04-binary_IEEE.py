# IEEE Binary Prefixes (base 2):

# The IEEE 1541 standard defines binary prefixes for powers of 2, which are
# used to represent data sizes in computing. These prefixes are based on
# powers of 1024 (2^10) and are commonly used to describe memory and storage
# capacities.

import scipy.constants as constants

print("IEEE Binary Prefixes:")
print("kibi (Ki):", constants.kibi)  # 2^10 = 1024
print("mebi (Mi):", constants.mebi)  # 2^20 = 1,048,576
print("gibi (Gi):", constants.gibi)  # 2^30 = 1,073,741,824
print("tebi (Ti):", constants.tebi)  # 2^40 = 1,099,511,627,776
print("pebi (Pi):", constants.pebi)  # 2^50 = 1,125,899,906,842,624
print("exbi (Ei):", constants.exbi)  # 2^60 = 1,152,921,504,606,846,976
print("zebi (Zi):", constants.zebi)  # 2^70 = 1,180,591,620,717,411,303,424
print("yobi (Yi):", constants.yobi)  # 2^80 = 1,208,925,819,614,629,174,706,176
