# HTML and CSS
# In this example, we will create a simple HTML page with some CSS styling.
# The page will display a heading, a paragraph, and a button. When the button
# is clicked, it will change the text of the paragraph.

# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Call the data from a CSV file.
csv_dest = 'https://'
csv_path = 'raw.githubusercontent.com/plotly/datasets/master/'
csv_file = 'gapminder2007'
csv_type = '.csv'
csv_location = [csv_dest + csv_path + csv_file + csv_type]

df: pd.DataFrame = pd.read_csv(csv_location[0])

css_dest = ['https://']
css_path = ['codepen.io/chriddyp/pen/']
css_file = ['bWLwgP']
css_type = ['.css']
external_stylesheets = [css_dest[0] + css_path[0] + css_file[0] + css_type[0]]

app = Dash(external_stylesheets=external_stylesheets)

# App layout
app.layout = [
    html.Div(
        className='row',
        children='Example App with Data, Graph, and Controls',
        style={
            'textAlign': 'center',
            'color': 'blue',
            'fontSize': 30
            }
    ),
    html.Div(
        className='row',
        children=[dcc.RadioItems(
          options=['pop', 'lifeExp', 'gdpPercap'],
          value='lifeExp',
          inline=True,
          id='my-radio-buttons-final'
        )]
    ),
    html.Div(
      className='row',
      children=[
        html.Div(
          className='six columns',
          children=[dag.AgGrid(
            rowData=df.to_dict('records'),
            columnDefs=[{"field": i} for i in df.columns]
            )]
        ),
        html.Div(
          className='six columns',
          children=[dcc.Graph(
            figure={},
            id='histo-chart-final'
            )]
        )]
    )
]


# Add controls to build the interaction
@callback(
    Output(
      component_id='histo-chart-final',
      component_property='figure'
    ),
    Input(
      component_id='my-radio-buttons-final',
      component_property='value'
    )
)
def update_graph(col_chosen):
    """ Update the graph based on the selected column.
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
