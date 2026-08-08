# Dash

# Dash is a Python framework for building analytical web applications.
# No JavaScript required. Built on top of Flask, Plotly.js, and React.js,
# Dash ties modern UI elements like dropdowns, sliders, and graphs directly to
# your analytical Python code.


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# I'm building a path management tool, sometimes breaking this data down is
# safer, manage version control, and allows for easier updates to the data
# source. This is a work in progress, and will be updated as the project
# progresses. The data source is from Plotly's datasets repository on GitHub.
# The dataset used in this example is the Gapminder dataset, which contains
# data on countries' GDP, life expectancy, and population over time.

# Add file SALT here to manage the data source.
# import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, 'example.txt')

csv_path = 'https://raw.githubusercontent.com/plotly/datasets/master/'
csv_file = 'gapminder_unfiltered.csv'
csv_location = csv_path + csv_file

df = pd.read_csv(csv_location)

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Example of Dash', style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    """ Update the graph based on the selected country.
    Parameters:
        value (str): The selected country from the dropdown.
    Returns:
        fig (plotly.graph_objs._figure.Figure): The updated figure to be
        displayed in the graph.
    Outcome:
        The graph will display the population over the years for the selected
        country.
        >>> update_graph('Canada')  # This will return a line graph of Canada's
        population over the years.

    """
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')


if __name__ == '__main__':
    app.run(debug=True)
