# Bi-Normal Distribution Example

# Bi-normal distribution is a continuous probability distribution for two
# variables that are normally distributed and may be correlated. It is
# defined by two means, two standard deviations, and a correlation
# coefficient. The distribution is often visualized as a 3D bell-shaped
# surface.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random bi-normal dataset
mean1, mean2 = 0, 0
covariance_matrix = [[1, 0.5], [0.5, 1]]
# Correlation between the two variables

data = np.random.multivariate_normal([mean1, mean2],
                                     covariance_matrix, size=1000)

# Plot the scatter plot of the bi-normal dataset
plt.scatter(data[:, 0], data[:, 1], alpha=0.2, color='orange')
plt.title('Bi-Normal Distribution Scatter Plot')
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.show()
