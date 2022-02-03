from dash.dependencies import Input, Output
import yfinance as yf
import pandas as pd

def register_callbacks(dashapp):

    @dashapp.callback(
        Output('main_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_table(ticker):

        t = yf.Ticker(ticker)

        main_table_columns = ['previousClose', 'open', 'currentPrice', 'bid', 'ask', 'dayLow', 'dayHigh', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh',
                         'volume', 'averageVolume', 'marketCap', 'beta']

        data = {}
        for k,v in t.info.items():
            if k in main_table_columns:
                data.update({k:v})

        series = pd.Series(data)
        df = pd.DataFrame(columns = main_table_columns)
        df = df.append(series, ignore_index = True)

        for format_col in ['volume', 'averageVolume', 'marketCap']:

            df[format_col] = df[format_col].apply(lambda x: f'{x:,.0f}')

        return df.to_dict('records')

    @dashapp.callback(
        Output('inst_holders_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_inst_table(ticker):

        t = yf.Ticker(ticker)
        df = pd.DataFrame(t.institutional_holders)

        for format_col in ['Shares', 'Value']:

            df[format_col] = df[format_col].apply(lambda x: f'{x:,.0f}')

        df['Date Reported'] = df['Date Reported'].apply(lambda x: x.date())

        return df.loc[:, ['Holder', 'Shares', 'Date Reported', 'Value']].to_dict('records')

    @dashapp.callback(
        Output('major_holder_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_major_table(ticker):

        t = yf.Ticker(ticker)
        df = pd.DataFrame(t.major_holders)
        df.rename(columns = {0: 'Percentage', 1: 'Holder'}, inplace = True)

        return df.to_dict('records')

    @dashapp.callback(
        Output('q_earnings_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_q_table(ticker):

        t = yf.Ticker(ticker)
        df = pd.DataFrame(t.quarterly_earnings)
        df['Quarter'] = df.index

        for format_col in ['Revenue', 'Earnings']:

            df[format_col] = df[format_col].apply(lambda x: f'{x:,.0f}')

        return df.to_dict('records')

    @dashapp.callback(
        Output('earnings_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_earnings_table(ticker):

        t = yf.Ticker(ticker)
        df = pd.DataFrame(t.earnings)
        df['Year'] = df.index

        for format_col in ['Revenue', 'Earnings']:

            df[format_col] = df[format_col].apply(lambda x: f'{x:,.0f}')

        return df.to_dict('records')
