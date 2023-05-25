from .models import Currency
from .exchange_info import get_current_price, get_24h_ticker


def update_currency_model(currencyObj : Currency):
    symbol = currencyObj.symbol + 'USDT'
    currencyObj.current_price = get_current_price(symbol)
    updated_data = get_24h_ticker(symbol)
    currencyObj.percent_change = float(updated_data['priceChangePercent'])
    currencyObj.percent_change = round(currencyObj.percent_change, 2)
    currencyObj.last_day_lowest_price = float(updated_data['lowPrice'])
    currencyObj.last_day_highest_price = float(updated_data['highPrice'])
    currencyObj.last_day_open_price = float(updated_data['openPrice'])
    currencyObj.save()
    return currencyObj









