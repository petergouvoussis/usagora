import os

path = os.path.abspath(os.path.dirname(__file__))

with open(f'{path}/nasdaq_screener.csv') as f:

    symbols = []
    for i in f.readlines()[1:]:
        if 'warrant' in i.lower():
            pass
        else:
            i = i.split(',')
            symbols.append(f'{i[0]} | {i[1]}')
