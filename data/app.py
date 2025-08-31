# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('formatted_sales.csv',parse_dates=['date'])


fig = px.line(df, x="date", y="sales", color='region')
fig.show()
app.layout = html.Div(children=[
    html.H1(children='Sales Trend Around Pink Morsel Price Change'),

    html.Div(children='''
        📈 Sales Visualiser: Pre vs Post Price Change
    '''),

    dcc.Graph(
        id='Sales Visualiser',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
