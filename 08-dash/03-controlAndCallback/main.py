# Control and Callback


# The following code demonstrates how to control and use callbacks in Dash,
# a Python framework for building analytical web applications. This example
# uses the Gapminder dataset, which contains data on countries' GDP, life
# expectancy, and population over time.

# You may notice I layout my code in a specific way. This is to make it easier
# to read and understand. I use type hints for variables and function
# arguments and also use PEP 257 docstrings for functions. Also with PEP 8,
# lint, and flake8.
# This is a coding style choice.

# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Call the data from a CSV file.
csv_path: str = 'https://raw.githubusercontent.com/plotly/datasets/master/'
csv_file: str = 'gapminder2007.csv'
csv_location: str = csv_path + csv_file

df: pd.DataFrame = pd.read_csv(csv_location)

# Initialise the app
app: Dash = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(
                   options=['pop', 'lifeExp', 'gdpPercap'],
                   value='lifeExp',
                   id='controls-and-radio-item'
                   ),
    dag.AgGrid(
                rowData=df.to_dict('records'),
                columnDefs=[{"field": i} for i in df.columns]
              ),
    dcc.Graph(
              figure={},
              id='controls-and-graph'
              )
]


# Add controls to build the interaction
@callback(
    Output(
           component_id='controls-and-graph',
           component_property='figure'
           ),
    Input(
           component_id='controls-and-radio-item',
           component_property='value'
           )
)
def update_graph(col_chosen):
    """Update the graph based on the selected column.
    Args:
        col_chosen (str): The column selected from the radio items.
    Returns:
        fig (plotly.graph_objs._figure.Figure): The updated figure based on
        the selected column.
    Output:
        The function returns a Plotly figure object that represents the
        updated graph based on the selected column from the radio items. The
        figure is created using Plotly Express's histogram function, which
        generates a histogram of the selected column's values grouped by
        continent. The histogram shows the average value of the selected
        column for each continent.
    """
    fig = px.histogram(
                       df,
                       x='continent',
                       y=col_chosen,
                       histfunc='avg'
                       )
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
