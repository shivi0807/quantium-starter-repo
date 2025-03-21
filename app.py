import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv('data/formatted_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Aggregate daily sales
df_daily = df.groupby('date', as_index=False)['sales'].sum()

# Dash app
app = Dash(__name__)

# Line chart
fig = px.line(df_daily,
              x='date',
              y='sales',
              title='Pink Morsel Sales Over Time',
              labels={'date':'Date', 'sales':'Total Sales ($)'})

# Mark price increase clearly without error
fig.add_shape(
    type="line",
    x0='2021-01-15', x1='2021-01-15',
    y0=df_daily['sales'].min(), y1=df_daily['sales'].max(),
    line=dict(color="red", width=2, dash="dash")
)

fig.add_annotation(
    x='2021-01-15', y=df_daily['sales'].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=1,
    ax=-100,
    ay=-40
)

# Layout
app.layout = html.Div([
    html.H1('Soul Foods Pink Morsel Sales Visualizer', style={'textAlign':'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

