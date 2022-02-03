# usagora

Dashboard (which allows user registration & login) showing data on U.S stock exchange listed companies. Built using Dash and Flask. Data sourced from yfinance. Deployed on Heroku.

## [https://usagora.herokuapp.com](https://usagora.herokuapp.com/)

Project Directory Structure:

```
.
│
├── app
│   │
│   ├── dashapps
│   │   │
│   │   ├── assets
│   │   │   └── style.css
│   │   │
│   │   ├── financials
│   │   │   ├── callbacks.py
│   ├   │   └── layout.py
│   │   │
│   │   ├── options
│   │   │   ├── callbacks.py
│   │   │   └── layout.py
│   │   │
│   │   ├── stocks
│   │   │   ├── callbacks.py
│   │   │   └── layout.py
│   │   │
│   │   └── index.py
│   │
│   ├── data
│   │   ├── nasdaq_screener.csv
│   │   └── symbols_list.py
│   │
│   ├── static
│   │   └── main.css
│   │
│   ├── templates
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── __init__.py
│   ├── extensions.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│   
├── database.db
├── run.py
⋮
```
