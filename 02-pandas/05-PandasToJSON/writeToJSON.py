# Write DataFrame to JSON file using pandas

# In this example, we will create a Pandas DataFrame and write it to a JSON
# file.

import os
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alex', 'Steve', 'Creeper', 'Herobrine', 'Enderman'],
    'Health': [100, 80, 20, 0, 50],
    'Level': [5, 4, 1, 0, 3]
}
df = pd.DataFrame(data)

# Define the path to the output JSON file
json_output_path = os.path.join(os.path.dirname(__file__), 'output.json')

# Write the DataFrame to a JSON file
df.to_json(json_output_path, orient='records', indent=4)
# Display a message indicating that the DataFrame has been written to the JSON
# file
print(f'DataFrame has been written to {json_output_path}')

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html

# The to_json function is used to write a DataFrame to a JSON file. It can
# handle various parameters to customize the writing process, such as
# specifying the orientation of the JSON data, handling missing values,
# and more.
