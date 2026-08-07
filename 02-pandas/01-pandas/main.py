# Pandas

# Pandas is a powerful data manipulation and analysis library for Python.
# It provides data structures like Series and DataFrame that make it easy to
# work with structured data.

# It is built on top of NumPy and is designed to work seamlessly with other
# libraries in the Python ecosystem, such as Matplotlib and SciPy.

# Pandas is widely used in data science, machine learning, and data analysis
# tasks.

# Official documentation: https://pandas.pydata.org/docs/user_guide/index.html
# GitHub repository: https://github.com/pandas-dev/pandas

# example of using pandas to create a DataFrame and perform basic operations
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alex', 'Steve', 'Creeper', 'Ghast'],
    'Health': [100, 80, 20, 50],
    'Attack': [10, 15, 5, 20]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Perform basic operations
# Calculate the average health
average_health = df['Health'].mean()
print("\nAverage Health:", average_health)
# Calculate the average attack
average_attack = df['Attack'].mean()
print("Average Attack:", average_attack)

# Filter the DataFrame to show only characters with health greater than 50
filtered_df = df[df['Health'] > 50]
print("\nCharacters with Health > 50:")
print(filtered_df)

# What this code does is it creates a DataFrame from a dictionary containing
# character names, health, and attack values. It then calculates the average
# health and attack values, and filters the DataFrame to show only characters
# with health greater than 50.
