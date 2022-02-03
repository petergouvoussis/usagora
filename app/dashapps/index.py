import dash_core_components as dcc
import dash_html_components as html

top_index = html.Div([
        html.Div([
        html.A(html.Button('LOGOUT', className = 'index-button', style = {'width': '5%', 'float': 'left'}), href='/logout'),
        html.A(html.Button('STOCKS', className = 'index-button', style = {'width': '5%', 'float': 'left','margin-left': '0.25%'}), href='/stocks'),
        html.A(html.Button('OPTIONS', className = 'index-button', style = {'width': '5%', 'float': 'left','margin-left': '0.1%'}), href='/options'),
        html.A(html.Button('FINANCIALS', className = 'index-button', style = {'width': '5%', 'float': 'left','margin-left': '0.1%'}), href='/financials')
        ], className = 'row'),
        html.Br(),
    ])
