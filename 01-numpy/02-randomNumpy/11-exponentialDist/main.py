# Exponential Distribution Example

# Exponential distribution is a continuous probability distribution that is
# often used to model the time between events in a Poisson process. It is
# defined by a single parameter, the rate parameter (lambda), which determines
# the average time between events. The exponential distribution is commonly
# used in reliability analysis, queuing theory, and survival analysis.

import numpy as np
import matplotlib.pyplot as plt
# Generate a random dataset with exponential distribution
data = np.random.exponential(scale=1.0, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='c')
plt.title('Exponential Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
