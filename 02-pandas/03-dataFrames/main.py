# Pandas DataFrames example

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Steve', 'Alex', 'Creeper', 'Herobrine'],
    'Health': [100, 80, 0, 100],
    'EXP': [0, 10, 0, 100]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Official documentation:
# https://pandas.pydata.org/docs/user_guide/index.html#dataframe

# Dataframes are two-dimensional, size-mutable, and heterogeneous tabular data
# structures with labeled axes (rows and columns). They can be thought of as a
# collection of Series objects that share the same index.

# Accessing columns:
print(df['Name'])
# Accessing rows:
print(df.loc[0])  # Access by index label
# Accessing rows by integer location:
print(df.iloc[0])  # Access by integer location

# Accessing specific elements:
print(df.at[0, 'Name'])  # Access by index label and column name
print(df.iat[0, 0])  # Access by integer location
