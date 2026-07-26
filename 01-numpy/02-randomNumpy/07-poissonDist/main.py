# Poisson Distribution Example

# Poisson distribution is a discrete probability distribution that expresses
# the probability of a given number of events occurring in a fixed interval of
# time or space, given the average number of times the event occurs over that
# interval. It is often used to model the number of events happening in a
# fixed period of time, such as the number of phone calls received by a call
# center in an hour or the number of decay events per unit time from a
# radioactive source.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with Poisson distribution
data = np.random.poisson(lam=3, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
plt.title('Poisson Distribution Histogram')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.show()
