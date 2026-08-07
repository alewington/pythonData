# Read CSV file using pandas
import os
import pandas as pd


# Locate the current working directory

# Read the CSV file into a DataFrame
base_dir = os.path.dirname(os.path.abspath(__file__))
# Get the directory of the current script
file_path = os.path.join(base_dir, 'output.csv')

df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("DataFrame from CSV:")
print(df.head())

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# The read_csv function is used to read a CSV file into a DataFrame. It can
# handle various parameters to customize the reading process, such as
# specifying the delimiter, handling missing values, and more.

# Check out 'WriteToCSV.py' to see how the CSV file was created.
