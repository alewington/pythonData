# Dash

# Dash is a Python framework for building analytical web applications.
# No JavaScript required.

# Dash is ideal for building data visualization apps with highly custom user
# interfaces in pure Python. It's particularly suited for anyone who works
# with data in Python.

# Dash apps are rendered in the web browser. You can deploy your apps to
# servers and share them via URLs.

# Dash is open source, and its apps can be deployed to servers and shared via
# URLs.

# Dash is built on top of Flask, Plotly.js, and React.js. It ties modern UI
# elements like dropdowns, sliders, and graphs directly to your analytical
# Python code.

# Import packages
from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# Input data from a CSV file. The dataset used in this example is the
# Gapminder dataset, which contains data on countries' GDP, life expectancy,
# and population over time.
csv_path = 'https://raw.githubusercontent.com/plotly/datasets/master/'
csv_file = 'gapminder2007.csv'
csv_location = csv_path + csv_file

df = pd.read_csv(csv_location)

# Initialise the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Example App with Data'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    )
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
