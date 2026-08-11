# Uniform Distribution Example

# Uniform distribution is a type of probability distribution in which all
# outcomes are equally likely. In a continuous uniform distribution,
# the probability of any value within a specified range is the same.
# It is often used to model random variables that have no bias towards
# any particular value within the range.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with uniform distribution
data = np.random.uniform(low=0, high=10, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='r')
plt.title('Uniform Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
