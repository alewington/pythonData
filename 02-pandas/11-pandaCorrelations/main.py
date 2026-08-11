# Pandas Correlations Example

# Correlation is a statistical measure that describes the strength and
# direction of the relationship between two variables. In pandas, we can
# easily compute the correlation between columns of a DataFrame using
# the `corr()` method. The correlation coefficient ranges from -1 to 1,
# where:
# - 1 indicates a perfect positive correlation,
# - -1 indicates a perfect negative correlation, and
# - 0 indicates no correlation.

import pandas as pd
# Visualize the correlation matrix using a heatmap
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Compute the correlation matrix
correlation_matrix = df.corr()
# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)


sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.show()

# What is the correlation between columns A and B?
correlation_A_B = correlation_matrix.loc['A', 'B']
print(f"Correlation between A and B: {correlation_A_B}")

# What is the correlation between columns A and C?
correlation_A_C = correlation_matrix.loc['A', 'C']
print(f"Correlation between A and C: {correlation_A_C}")

# What is the correlation between columns B and C?
correlation_B_C = correlation_matrix.loc['B', 'C']
print(f"Correlation between B and C: {correlation_B_C}")

# The correlation matrix provides a quick overview of the relationships
# between the variables in the DataFrame. In this example, we can see that
# columns A and B have a perfect negative correlation (-1),
# while columns A and C have a perfect positive correlation (1),
# columns B and C also have a perfect negative correlation (-1).

# This means that as the values in column A increase, the values in column B
# decrease, and vice versa. Similarly, as the values in column A increase, the
# values in column C also increase. Understanding these relationships can help
# in making informed decisions based on the data.
