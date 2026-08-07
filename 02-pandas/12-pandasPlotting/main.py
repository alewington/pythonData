# pandas plotting

# pandas provides built-in plotting capabilities using the matplotlib library.
# You can create various types of plots, such as line plots, bar plots,
# histograms, and scatter plots, directly from pandas DataFrames and Series.

import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Name': ['Steve', 'Creeper', 'Alex', 'Herobrine', 'Enderman'],
    'Health': [100, 0, 100, 50, 100],
    'Hit Points': [10, 0, 10, 5, 10]
}
df = pd.DataFrame(data)

# Plot data on the same graph as a line plot.
plt.figure(figsize=(8, 5))

# Plotting health of a character
plt.plot(df['Name'], df['Health'], marker='o',
         linestyle='-', color='b', label='Health')

# Plotting hit points of a character
plt.plot(df['Name'], df['Hit Points'], marker='x',
         linestyle='--', color='r', label='Hit Points')

plt.title('Health and Hit Points of Characters')
plt.xlabel('Character Name')
plt.ylabel('Values')
plt.grid()
plt.legend()
plt.show()
