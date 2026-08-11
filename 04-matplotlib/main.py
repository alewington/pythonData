# Matplotlib

# Matplotlib is a Python library used for creating static, animated, and
# interactive visualizations. It is highly customizable and works well with
# NumPy and Pandas.

# To install Matplotlib, you can use either conda or pip. Here are the
# commands for both:

# Using conda:
# conda install matplotlib

# Using pip:
# pip install matplotlib

# You can also update Matplotlib using the following commands:

# Using conda:
# conda update matplotlib

# Using pip:
# pip install --upgrade matplotlib

# To check if Matplotlib is installed and to see its version, you can run the
# following command in your Python environment:

# python -c "import matplotlib; print(matplotlib.__version__)"

# example usage of Matplotlib:
import os  # for file path operations
import sys  # needed to draw the plot in some environments
import matplotlib  # needed to draw the plot in some environments
import matplotlib.pyplot as plt  # for plotting graphs
import numpy as np  # for numerical operations
matplotlib.use('Agg')  # needed to draw the plot in some environments

# Creating a simple line plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

base_dir = os.path.dirname(os.path.abspath(__file__))
# Get the directory of the current script
file_path = os.path.join(base_dir, 'example.png')
# Create a file path for the PNG file

# Two  lines to make our compiler able to draw:
plt.savefig(file_path)
# Save the plot as a PNG file
sys.stdout.flush()
# Flush the output buffer to ensure the plot is displayed in some environments

# This code is for data analysis using Python. It includes importing necessary
# libraries and setting up the environment for data analysis tasks. It is
# broken into sections for better understanding and organization.
# Each section will cover different aspects of data analysis, including
# data manipulation, visualization, and statistical analysis. You will need to
# have a good grasp of Python programming and data analysis concepts to
# effectively use this code. Make sure to have the required libraries
# installed and the virtual environment activated before running the code.
# Please see Python Basics for a refresher on Python programming concepts.
#

# Goto:
# https://matplotlib.org/stable/users/getting_started/
# https://matplotlib.org/cheatsheets/
# https://matplotlib.org/stable/plot_types/index.html
