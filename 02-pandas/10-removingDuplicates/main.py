# Removing Duplicates

# In this notebook, we will learn how to remove duplicate data in a pandas
# DataFrame. Duplicate data can occur when multiple rows have the same values
# across all or specific columns. We will explore different methods to handle
# duplicate data, including dropping duplicate rows and keeping the first or
# last occurrence.

import pandas as pd

# Create a sample DataFrame with duplicate values
data = {
    'Name': ['Steve', 'Creeper', 'Alex', 'Steve', 'Herobrine', 'Alex'],
    'Health': [100, 0, 100, 100, 50, 100],
    'Hit Points': [10, 0, 10, 10, 5, 10]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Handling Duplicate Values
# Drop duplicate rows based on all columns
df_dropped_duplicates = df.drop_duplicates()
print("DataFrame after dropping duplicate rows based on all columns:")
print(df_dropped_duplicates)

# Drop duplicate rows based on a specific column (e.g., 'Name')
df_dropped_duplicates_name = df.drop_duplicates(subset='Name')
print("DataFrame after dropping duplicate rows based on the 'Name' column:")
print(df_dropped_duplicates_name)

# Keep the last occurrence of duplicate rows based on all columns
df_keep_last = df.drop_duplicates(keep='last')
print("DataFrame after keeping the last occurrence of duplicate rows based on",
      "all columns:")
print(df_keep_last)
