# Visualise Data with Dash

# The following code demonstrates how to visualize data using Dash,
# a Python framework for building analytical web applications.
# This example uses the Gapminder dataset, which contains data on countries'
# GDP, life expectancy, and population over time.


# Import packages
from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Call the data from a CSV file. The dataset used in this example is the
# Gapminder dataset, which contains data on countries' GDP, life expectancy,
# and population over time. From plotly's datasets repository on GitHub,
# the dataset is accessed via a URL.

csv_path = 'https://raw.githubusercontent.com/plotly/datasets/master/'
csv_file = 'gapminder2007.csv'
csv_location = csv_path + csv_file

df = pd.read_csv(csv_location)


# Initialise the app
app = Dash()

# App layout for table and graph.
app.layout = [
    html.Div(children='Example App with Data and a Graph'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    ),
    dcc.Graph(figure=px.histogram(
                                  df,
                                  x='continent',
                                  y='lifeExp',
                                  histfunc='avg'
                                  ))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
