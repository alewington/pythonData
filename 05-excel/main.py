# Excel file manipulation

import openpyxl
import os  # for file path operations

# openpyxl is a Python library used for reading and writing Excel files
# (with .xlsx extension). It allows you to create, modify, and extract data
# from Excel spreadsheets.

# To install openpyxl, you can use either conda or pip. Here are the commands
# for both:

# Using conda:
# conda install openpyxl

# Using pip:
# pip install openpyxl

# You can also update openpyxl using the following commands:

# Using conda:
# conda update openpyxl

# Using pip:
# pip install --upgrade openpyxl

# To check if openpyxl is installed and to see its version, you can run the
# following command in your Python environment:

# python -c "import openpyxl; print(openpyxl.__version__)"

# example usage of openpyxl:

# Creating a new Excel workbook
workbook = openpyxl.Workbook()
# Creating a new sheet in the workbook
sheet = workbook.active or workbook.create_sheet()

# Adding data to the sheet
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['A3'] = 'Bob'
sheet['B3'] = 25

# Saving the workbook to a file
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'example.xlsx')

workbook.save(file_path)

# This code is for Excel file manipulation using Python. It includes importing
# necessary libraries and setting up the environment for Excel file
# operations. It is broken into sections for better understanding and
# organisation.
