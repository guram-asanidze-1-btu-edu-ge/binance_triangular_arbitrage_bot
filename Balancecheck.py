import time
import threading
import schedule
from datetime import datetime
import math
import aiohttp
import schedule
from binance.client import Client
import keys
def balance():
    api_key = keys.api_key1
    api_secret = keys.secret_key1
    client = Client(api_key, api_secret)
    account_info = client.get_account()
    balances = account_info['balances']

    usdt_balance = 0.0
    other_currencies_balance = 0.0

    excluded_currencies = ['SOL', 'XRP', 'DOGE', 'SHIB']

    for balance in balances:
        asset = balance['asset']
        free_balance = float(balance['free'])

        if free_balance > 0.0:
            if asset != 'USDT' and asset != 'TRY' and asset != 'BRL':
                trading_pair = f'{asset}USDT'
                try:
                    ticker_price = client.get_symbol_ticker(symbol=trading_pair)
                    asset_price = float(ticker_price['price'])
                    usdt_equivalent = free_balance * asset_price
                    if asset not in excluded_currencies:
                        other_currencies_balance += usdt_equivalent
                except Exception as e:
                    if trading_pair == 'TRYUSDT' or trading_pair == 'BRLUSDT':
                        print(f'Failed to retrieve ticker price for {trading_pair}: {e}')
                    else:
                        raise e
            elif asset == 'TRY' or asset == 'BRL':
                trading_pair = f'USDT{asset}'
                try:
                    ticker_price = client.get_symbol_ticker(symbol=trading_pair)
                    asset_price = float(ticker_price['price'])
                    usdt_equivalent = free_balance / asset_price
                    other_currencies_balance += usdt_equivalent
                except Exception as e:
                    if trading_pair == 'USDTTRY' or trading_pair == 'USDTBRL':
                        print(f'Failed to retrieve ticker price for {trading_pair}: {e}')
                    else:
                        raise e
            else:
                usdt_balance += free_balance


    total_balance = usdt_balance + other_currencies_balance
    current_datetime = datetime.now()
    print(current_datetime)
    print(f'Total USDT Balance: {usdt_balance}')
    print(f'Total Other Currencies Balance: {other_currencies_balance}')
    print(f'Total Balance (excluding : {total_balance}')
def shd():
    try:
        schedule.every(1).seconds.do(balance)
        while True:
            schedule.run_pending()

    except Exception as e:
        print(e)
        shd()


shd()
