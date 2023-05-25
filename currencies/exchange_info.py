import os

from binance import Client

apikey = os.getenv('API_KEY')
secret = os.getenv('SECRET_KEY')

client = Client(apikey, secret)

def get_current_price(symbol : str) -> float:
    requested_price = client.get_symbol_ticker(symbol = symbol)
    return round(float(requested_price['price']), 5)

def get_24h_ticker(symbol : str):
    ticker_response = client.get_ticker(symbol = symbol)
    return ticker_response


