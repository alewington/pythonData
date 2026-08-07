# Analysing JSON data using Pandas

# In this example, we will read JSON data from a file and perform some basic
# analysis using Pandas.

import os
import pandas as pd

# Define the path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'output.json')
# Read the JSON file into a DataFrame
df = pd.read_json(json_file_path, orient='records')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Perform basic analysis on the DataFrame
# Calculate the average health of the characters
average_health = df['Health'].mean()
print(f"\nAverage Health of characters: {average_health}")

# Count the number of characters at each level
level_counts = df['Level'].value_counts()
print("\nNumber of characters at each level:")
print(level_counts)

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html

# The mean function is used to calculate the average of a numerical column in
# the DataFrame, while the value_counts function is used to count the
# occurrences of each unique value in a column. These functions are useful for
# performing basic analysis on the data.
