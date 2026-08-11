# Zipf Distribution Example

# Zipf distribution is a discrete probability distribution that describes the
# frequency of elements in a dataset, where the frequency of an element is
# inversely proportional to its rank in the frequency table. In other words,
# the most frequent element occurs approximately twice as often as the second
# most frequent element, three times as often as the third most frequent
# element, and so on. The Zipf distribution is often used to model the
# distribution of words in natural languages, city populations, and other
# phenomena that exhibit a power-law behavior.

import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with Zipf distribution
data = np.random.zipf(a=2.0, size=1000)
# Plot the histogram of the dataset
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
plt.title('Zipf Distribution Histogram')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.show()
