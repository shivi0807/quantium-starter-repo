import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Initialize app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

# Define layout
app.layout = html.Div(className="main-container", children=[
    html.Div(className="header", children=[
        html.H1("Pink Morsel Sales", className="title", id="main-header"),  # 👈 ID added here
        html.P("Interactive region-based sales analysis", className="subtitle")
    ]),

    html.Div(className="controls", children=[
        html.Label("Choose Region:", className="region-label"),
        dcc.RadioItems(
            id='region-selector',  # ✅ Already good
            options=[{'label': region.capitalize(), 'value': region}
                     for region in ['north', 'east', 'south', 'west', 'all']],
            value='all',
            className="radio-buttons"
        )
    ]),

    html.Div(className="graph-container", children=[
        dcc.Graph(id='sales-graph')  # ✅ Already good
    ])
])

# Callback to update the chart based on region
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == region]

    # Group data by date and sum sales
    plot_df = filtered.groupby('date')['sales'].sum().reset_index()

    # Create the line chart
    fig = px.line(
        plot_df,
        x='date',
        y='sales',
        title=f"{region.capitalize()} Region Sales" if region != 'all' else "All Regions Sales",
        template='plotly_white'
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(l=40, r=40, t=60, b=40),
        hovermode="x unified"
    )
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
