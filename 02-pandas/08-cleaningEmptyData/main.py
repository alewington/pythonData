# Cleaning Empty Data

# In this notebook, we will learn how to clean empty data in a pandas
# DataFrame. Empty data can be represented as NaN (Not a Number) or None in
# pandas. We will explore different methods to handle missing values,
# including dropping rows or columns with missing data and filling missing
# values with specific values.

import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'Name': ['Steve', 'Creeper', 'Alex', None, 'Herobrine'],
    'Health': [100, 0, 100, 50, None],
    'Hit Points': [10, 0, 10, None, 5]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")

print(df)

# Handling Missing Values
# Drop rows with any missing values
df_dropped = df.dropna()
print("DataFrame after dropping rows with any missing values:")
print(df_dropped)

# Fill missing values with a specific value
df_filled = df.fillna({'Name': 'Unknown', 'Health': 0,
                       'Hit Points': 0})
print("DataFrame after filling missing values:")
print(df_filled)

# Drop columns with any missing values
df_dropped_columns = df.dropna(axis=1)
print("DataFrame after dropping columns with any missing values:")
print(df_dropped_columns)

# Summary
# In this notebook, we learned how to clean empty data in a pandas DataFrame.
# We explored methods to drop rows or columns with missing values and fill
# missing values with specific values. Handling missing data is an essential
# step in data preprocessing to ensure the quality and integrity of the
# dataset.
