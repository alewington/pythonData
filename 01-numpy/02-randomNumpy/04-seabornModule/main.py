# Seaborn Module

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and informative
# statistical graphics.

# Seaborn works well with pandas data structures and provides functions to
# visualize univariate and bivariate data, as well as to fit and visualize
# linear regression models.

# Seaborn can be installed using pip or conda. To install Seaborn, you can use
# the following command:
# pip install seaborn
# or
# conda install seaborn

# Create a random dataset
data = np.random.normal(size=100)
sns.histplot(data, kde=True)

plt.show()
# needs to be run in live terminal with possibly jupiter notebook or other
# IDEs that support inline plotting.
# if using ssh to connect to python environment, use X11 forwarding to display
# the plot on your local machine.
