# Write DataFrame to CSV file using pandas
import os
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Steve', 'Alex', 'Creeper'],
    'Health': [100, 80, 60],
    'Damage': [10, 15, 20]
}
df = pd.DataFrame(data)

# locate the current working directory
base_dir = os.path.dirname(os.path.abspath(__file__))
# Get the directory of the current script
file_path = os.path.join(base_dir, 'output.csv')
# Define the output file path

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)

# Official documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# The to_csv function is used to write a DataFrame to a CSV file. It can
# handle various parameters to customize the writing process, such as
# specifying the delimiter, whether to include the index, and more.
