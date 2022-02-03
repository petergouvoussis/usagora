import dash_core_components as dcc
import dash_html_components as html
from app.data.symbols_list import symbols
from app.dashapps.index import top_index

layout = html.Div([
    html.Div([
        top_index,
        html.H2(children = 'NYSE / NASDAQ / AMEX'),
        html.Label('(6,831 tickers)'),
        dcc.Dropdown(id = 'drop_select', options = [{'label' : i, 'value': i.split('|')[0].strip()} for i in symbols],
                     value = ['TM', 'HMC', 'RACE'], multi = True)]),
    html.Br(),
    html.Div([
        html.Label('Time period:'),
        dcc.Dropdown(id = 'time_period_select', options = [{'label': i, 'value':i} for i in ['1d','5d','1mo','6mo','1y','5y','max']],
                     value = '1mo')], style = {'display': 'inline-block', 'width': '11%'}),
    html.Br(),
    html.Br(),
    html.Div([
        html.Label('Y-axis:'),
        dcc.RadioItems(id = 'linearpercent', options = [{'label': i, 'value':i} for i in ['Linear', 'Percent']], value = 'Percent', style = {'display': 'inline-block', 'width': '15%'}),
        html.Br(),
        html.Label('Include pre/post market hours data:'),
        dcc.RadioItems('prepost', options = [{'label': i, 'value':i} for i in ['True', 'False']], value = 'False', style = {'display': 'inline-block', 'width': '15%'}),
        dcc.Graph(id = 'main_chart', style = {'height': '615px'})
     ])])
