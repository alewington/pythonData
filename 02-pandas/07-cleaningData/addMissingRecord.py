# Adding a missing record to a JSON file using Pandas
# In this example, we will read JSON data from a file, add a new record to the
# DataFrame, and then write the updated DataFrame back to the JSON file.
import os
import pandas as pd

# Define the path to the input JSON file
json_input_path = os.path.join(os.path.dirname(__file__), 'output.json')
# Read the JSON file into a DataFrame
df = pd.read_json(json_input_path, orient='records')

# Add empty record to the DataFrame
empty_record = {'Name': '', 'Health': None, 'Level': None}
df = pd.concat([df, pd.DataFrame([empty_record])], ignore_index=False)
# Display the updated DataFrame with the empty record
print("\nUpdated DataFrame after adding an empty record:")
print(df)
# Write the updated DataFrame with the empty record back to the JSON file
df.to_json(json_input_path, orient='records', indent=4)
# Display a message indicating that the updated DataFrame with the empty record
# has been written to the JSON file
print('\nUpdated DataFrame with empty record has been written to',
      f'{json_input_path}')
# this record will be used to demonstrate how to handle missing data in the
# next example.
