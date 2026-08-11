# Normal Distribution Example

# Normal distribution is a continuous probability distribution that is
# symmetric about the mean, showing that data near the mean are more
# frequent in occurrence than data far from the mean. In graph form,
# normal distribution will appear as a bell curve.

# The normal distribution is defined by two parameters: the mean (average) and
# the standard deviation (which measures the spread of the data). The mean
# determines the center of the distribution, while the standard deviation
# determines the width of the bell curve.

import numpy as np
import matplotlib.pyplot as plt
# Generate a random dataset with normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)


# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.show()

# The histogram shows the frequency distribution of the dataset, and it should
# resemble a bell curve, indicating that the data follows a normal
# distribution.
