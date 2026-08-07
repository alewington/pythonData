# pandas

# pandas is a powerful library for data manipulation and analysis in Python.
# It provides data structures like Series and DataFrame to efficiently handle
# and analyze structured data. It is widely used in data analysis, finance,
# and scientific computing due to its efficiency and ease of use.

# https://pandas.pydata.org/docs/user_guide/index.html
# https://github.com/pandas-dev/pandas

# To install pandas, you can use either conda or pip. Here are the commands for
# both:

# Using conda:
# conda install pandas

# Using pip:
# pip install pandas

# You can also update pandas using the following commands:

# Using conda:
# conda update pandas

# Using pip:
# pip install --upgrade pandas

# To check if pandas is installed and to see its version, you can run the
# following command in your Python environment:

# python -c "import pandas; print(pandas.__version__)"

# example usage of pandas:
import pandas as pd

# Creating a Series
series = pd.Series([1, 2, 3, 4, 5, 6])

# Creating a DataFrame
data = {
    'Name': ['Steve', 'Creeper', 'Alex', 'Steve', 'Herobrine', 'Alex'],
    'Health': [100, 0, 100, 100, 50, 100],
    'Hit Points': [10, 0, 10, 10, 5, 10]
}
df = pd.DataFrame(data)

# Display the Series and DataFrame
print("Series:")
print(series)
print("\nDataFrame:")
print(df)
