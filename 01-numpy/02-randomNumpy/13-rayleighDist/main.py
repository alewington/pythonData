# Rayleigh Distribution Example

# Rayleigh distribution is a continuous probability distribution that is
# often used to model the magnitude of a two-dimensional vector whose
# components are independent and normally distributed with equal variance.
# It is defined by a single parameter, the scale parameter (sigma), which
# determines the spread of the distribution. The Rayleigh distribution is
# commonly used in signal processing, reliability analysis, and in modeling
# the distribution of wind speeds.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with Rayleigh distribution
data = np.random.rayleigh(scale=1.0, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='y')
plt.title('Rayleigh Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
