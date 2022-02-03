from dash_table import DataTable
import dash_core_components as dcc
import dash_html_components as html
from app.data.symbols_list import symbols
from app.dashapps.index import top_index

main_table_columns = ['previousClose', 'open', 'currentPrice', 'bid', 'ask', 'dayLow', 'dayHigh', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh',
                 'volume', 'averageVolume', 'marketCap', 'beta']

inst_holders_columns = ['Holder', 'Shares', 'Date Reported', 'Value']

layout = html.Div([
    top_index,
    html.H2('FINANCIAL AND TRADE DATA'),
    html.Br(),
    html.Div([
        html.Label('Ticker:'),
        dcc.Dropdown(id = 'ticker_select', options = [{'label' : i, 'value': i.split('|')[0].strip()} for i in symbols], value = 'F')
        ], style = {'display': 'inline-block', 'width': '64.5%'}),
    html.Br(),
    html.Br(),
    DataTable(id='main_table', columns=[{'name': i, 'id': i} for i in main_table_columns], data=[]),
    html.Br(),
    html.Div([
        html.Div([
            DataTable(id='q_earnings_table', columns = [{'name': i, 'id': i} for i in ['Quarter', 'Revenue', 'Earnings']], data=[]),
            html.Br(),
            DataTable(id='earnings_table', columns = [{'name': i, 'id': i} for i in ['Year', 'Revenue', 'Earnings']], data=[])
        ], className = 'column', style = {'width': '25%', 'float': 'left'}),
        html.Div([
            DataTable(id='inst_holders_table', columns = [{'name': i, 'id': i} for i in inst_holders_columns], data=[])
        ], style = {'width': '51%', 'float': 'left', 'margin-left': '1%'}),
        html.Div([
            DataTable(id='major_holder_table', columns = [{'name': i, 'id': i} for i in ['Percentage', 'Holder']], data=[])
        ], style = {'width': '22%', 'float': 'left', 'margin-left': '1%'})
    ])
    ])
