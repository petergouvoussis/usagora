from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import yfinance as yf

def register_callbacks(dashapp):

    @dashapp.callback(
        Output('main_chart', 'figure'),
        [Input('drop_select', 'value'),
         Input('time_period_select', 'value'),
         Input('linearpercent', 'value'),
         Input('prepost', 'value')])
    def update_chart(ticker, time_period, lin_per, pre_post):
        d = {'1d': '1m', '5d': '1m', '1mo': '5m'}

        df = pd.DataFrame(columns = ['Close', 'period_open_price', 'Symbol', 'percent_delta'])
        for t in ticker:
            output = pd.DataFrame(yf.Ticker(t).history(period = time_period, interval = d.get(time_period, '1d'), prepost = pre_post))
            output['Symbol'] = t
            output['period_open_price'] = output['Close'][0]
            output['percent_delta'] = round((((output['Close'] - output['period_open_price']) / output['period_open_price']) * 100), 2)
            output = output.loc[:, ['Close', 'period_open_price', 'Symbol', 'percent_delta']]
            df = pd.concat([df, output])

        if lin_per == 'Linear':
            y_var = 'Close'
            y_label = 'Price ($)'
        else:
            y_var = 'percent_delta'
            y_label = '% change'

        if time_period in d.keys():
            if pre_post == 'True':
                ranges = [dict(bounds = ['sat', 'mon']), dict(bounds = [20, 6.5], pattern = 'hour'), dict(values = ['2022-01-17 06:30:00-00:00'])]
            else:
                ranges= [dict(bounds = ['sat', 'mon']), dict(bounds = [16, 9.5], pattern = 'hour'), dict(values = ['2022-01-17 09:30:00-00:00'])]
        else:
            ranges = [dict(bounds = ['sat', 'mon']), dict(values = ['2022-01-17'])]

        fig = px.line(df, x = df.index, y = y_var, color = 'Symbol', render_mode = 'svg')
        fig.update_xaxes(title = 'Datetime (EST)', rangebreaks = ranges, showspikes = True, spikedash = 'dot', spikemode = 'toaxis',
                         spikesnap = 'hovered data')
        fig.update_yaxes(title = y_label, showspikes = True, spikedash = 'dot', spikemode = 'toaxis',
                         spikesnap = 'hovered data')
        fig.update_traces(connectgaps = True)
        fig.update_layout(paper_bgcolor = "rgba(0,0,0,0)")
        return fig
