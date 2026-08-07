# Pandas Series

# A Pandas Series is a one-dimensional array-like data structure that can hold
# data of any type (integer, float, string, etc.). It is similar to a column
# in a DataFrame.

# Official documentation:
# https://pandas.pydata.org/docs/user_guide/index.html#series

import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Series:")
print(series)
