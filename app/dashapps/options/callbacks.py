from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import yfinance as yf

def register_callbacks(dashapp):

    @dashapp.callback(
        Output('main_table', 'data'),
        [Input('ticker_select', 'value')])
    def update_table(ticker):

        t = yf.Ticker(ticker)

        df_calls = pd.DataFrame(columns = ['Expiration Date', 'ITM (Calls)', 'OTM (Calls)'])
        df_puts = pd.DataFrame(columns = ['Expiration Date', 'ITM (Puts)', 'OTM (Puts)'])

        for date in t.options:

            df = pd.DataFrame(t.option_chain(date).calls)
            df = df.loc[:,['volume', 'inTheMoney']]
            df = df.dropna(subset = ['volume'])
            ITM = int(df.loc[df['inTheMoney'] == True, 'volume'].sum())
            OTM = int(df['volume'].sum() - ITM)

            df_calls = df_calls.append({'Expiration Date': date, 'ITM (Calls)': ITM, 'OTM (Calls)': OTM}, ignore_index = True)

            df = pd.DataFrame(t.option_chain(date).puts)
            df = df.loc[:,['volume', 'inTheMoney']]
            df = df.dropna(subset = ['volume'])
            ITM = int(df.loc[df['inTheMoney'] == True, 'volume'].sum())
            OTM = int(df['volume'].sum() - ITM)

            df_puts = df_puts.append({'Expiration Date': date, 'ITM (Puts)': ITM, 'OTM (Puts)': OTM}, ignore_index = True)

        df = df_calls.merge(df_puts, on = 'Expiration Date')
        return df.to_dict('records')

    @dashapp.callback(
        Output('current_price', 'children'),
        [Input('ticker_select', 'value')])
    def display_current_price(ticker):

        price = yf.Ticker(ticker).info['currentPrice']

        return f'Current price: ${price}'
