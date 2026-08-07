# Reading JSON data from a file

# In this example, we will read JSON data from a file and convert it into a
# Pandas DataFrame.
import os
import pandas as pd

# Define the path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'output.json')
# Read the JSON file into a DataFrame
df = pd.read_json(json_file_path, orient='records')

# Display the first few rows of the DataFrame
print(df.head())

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.read_json.html

# The read_json function is used to read a JSON file into a DataFrame. It can
# handle various parameters to customize the reading process, such as
# specifying the orientation of the JSON data, handling missing values,
# and more.
