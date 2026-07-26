# Multinomial Distribution Example

# Multinomial distribution is a generalization of the binomial distribution
# to more than two outcomes. It describes the probabilities of obtaining a
# specific combination of outcomes in a fixed number of trials, where each
# trial can result in one of several possible outcomes. The multinomial
# distribution is often used in scenarios where there are multiple categories
# or classes, such as rolling a die or drawing colored balls from a bag.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with multinomial distribution
n_trials = 10  # Number of trials
probabilities = [0.2, 0.5, 0.3]
data = np.random.multinomial(n_trials, probabilities, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Multinomial Distribution Histogram')
plt.xlabel('Number of Outcomes')
plt.ylabel('Probability')
plt.show()
