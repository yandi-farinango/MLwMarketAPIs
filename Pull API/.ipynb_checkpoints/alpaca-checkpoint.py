# -*- coding: utf-8 -*-
"""Alpaca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13d1jDtseiH7F_7ZKZTjMuF7iA4fJ11iZ
"""

!pip install alpaca_trade_api

import alpaca_trade_api as tradeapi

# Replace these with your API connection info from the dashboard
base_url = 'https://paper-api.alpaca.markets'
api_key_id = 'PKILAPPNNLK7DKUDD3V4'
api_secret = '9m70crwYrofvh7Xyt5D3786iq9uP2yNhRMfUetcH'

api = tradeapi.REST(
    base_url=base_url,

    key_id=api_key_id,
    secret_key=api_secret
)

api. get_account()

assets = api.list_assets()
print("\nassets: ")
print(assets[0:10])
positions = api.list_positions()
print("\npositions: ")
print(positions)
api.submit_order('AAPL',10,'buy','limit','gtc',170.50)
orders = api.list_orders()
print("\norders: ")
print(orders)

api.submit_order('AAPL', side='buy', qty=1, type='market', time_in_force='gtc')

api.get_barset('AAPL', 'day', limit=10).df