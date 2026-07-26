# Logistic Distribution Example

# Logistic distribution is a continuous probability distribution that is
# often used to model growth processes and is similar in shape to the normal
# distribution but has heavier tails. It is defined by two parameters: the
# location parameter (mean) and the scale parameter (which determines the
# spread of the distribution). The logistic distribution is commonly used in
# logistic regression and in modeling the growth of populations.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with logistic distribution
data = np.random.logistic(loc=0, scale=1, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='m')
plt.title('Logistic Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
