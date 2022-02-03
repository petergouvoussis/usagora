from dash_table import DataTable
import dash_core_components as dcc
import dash_html_components as html
from app.data.symbols_list import symbols
from app.dashapps.index import top_index

table_columns = ['Expiration Date', 'ITM (Calls)', 'OTM (Calls)', 'ITM (Puts)', 'OTM (Puts)']

layout = html.Div([
    top_index,
    html.H2('OPTIONS DATA'),
    html.Label('Call & Put contracts expiring ITM (In The Money) and OTM (Out The Money).'),
    html.Br(),
    html.Br(),
    html.Div([
        html.Label('(6,831 tickers)'),
        dcc.Dropdown(id = 'ticker_select', options = [{'label' : i, 'value': i.split('|')[0].strip()} for i in symbols], value = 'TSLA')],
        style = {'display': 'inline-block', 'width': '64.5%'}),
    html.Br(),
    html.Br(),
    html.Div(id = 'current_price'),
    DataTable(id='main_table', columns=[{"name": i, "id": i} for i in table_columns], data=[])
    ])
