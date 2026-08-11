# Cleaning JSON data using Pandas

# In this example, we will read JSON data from a file, clean it using Pandas,
# and then write the cleaned data back to a new JSON file.

import os
import pandas as pd

# Define the path to the input JSON file
json_input_path = os.path.join(os.path.dirname(__file__), 'output.json')
# Read the JSON file into a DataFrame
df = pd.read_json(json_input_path, orient='records')

# Display the first few rows of the DataFrame before cleaning
# show null rows
print("DataFrame before cleaning:")
print(df)

# Clean the DataFrame by removing rows with missing values
df_cleaned = df.dropna()

# Display the first few rows of the cleaned DataFrame
print("\nDataFrame after cleaning:")
print(df_cleaned)
# Write the cleaned DataFrame to a new JSON file
json_output_path = os.path.join(os.path.dirname(__file__),
                                'cleaned_output.json')
df_cleaned.to_json(json_output_path, orient='records', indent=4)
# Display a message indicating that the cleaned DataFrame has been written to
# the new JSON file
print(f'\nCleaned DataFrame has been written to {json_output_path}')

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html

# The dropna function is used to remove rows with missing values from the
# DataFrame. This is a common data cleaning step to ensure that the data is
# complete and ready for analysis. After cleaning the data, we write the
# cleaned DataFrame to a new JSON file using the to_json function.
