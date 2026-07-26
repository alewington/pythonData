# Chi-Square Distribution Example

# Chi-square distribution is a continuous probability distribution that is
# often used in hypothesis testing and statistical inference. It is defined by
# a single parameter, the degrees of freedom (df), which determines the shape
# of the distribution. The chi-square distribution is commonly used in tests of
# independence, goodness-of-fit tests, and in the construction of confidence
# intervals for variance.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with chi-square distribution
data = np.random.chisquare(df=2, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
plt.title('Chi-Square Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
