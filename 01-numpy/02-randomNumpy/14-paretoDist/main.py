# Pareto Distribution Example

# Pareto distribution is a continuous probability distribution that is
# often used to model the distribution of wealth, income, or other
# quantities that follow a power-law behavior. It is defined by a
# shape parameter (alpha), which determines the "heaviness" of the
# distribution's tail. The Pareto distribution is commonly used in
# economics, finance, and risk analysis.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with Pareto distribution
data = np.random.pareto(a=2.0, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Pareto Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()
