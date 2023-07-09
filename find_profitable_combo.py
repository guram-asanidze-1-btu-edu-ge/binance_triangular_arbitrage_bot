import time
import threading
import schedule
import math
import aiohttp
from binance.client import Client
import keys
api_key=keys.api_key1
api_secret=keys.secret_key1
def calculate_profit(pair, client):
    def calcul(symbol):
        # Specify the trading pair symbol
        symbol_info = client.get_symbol_info(symbol)

        # Find the 'LOT_SIZE' filter and extract the minQty value
        min_qty_filter = next(filter(lambda f: f['filterType'] == 'LOT_SIZE', symbol_info['filters']), None)
        if min_qty_filter:
            min_qty = float(min_qty_filter['minQty'])
        else:
            min_qty = 0

        number_string = str(min_qty)
        count = 0

        for digit in number_string:
            if digit == '0':
                count += 1
            elif digit == '.':
                count = 0  # Reset count if decimal point is encountered
            elif digit == '1':
                count += 1
                break

        multipliers = {
            7: 10000000,
            6: 1000000,
            5: 100000,
            4: 10000,
            3: 1000,
            2: 100,
            1: 1,
            0: 1
        }
        return multipliers[count]
    try:
        leg1 = pair['leg1']
        leg2 = pair['leg2']
        leg3 = pair['leg3']

        # Check if the market is closed for any of the trading pairs
        is_market_closed = False
        exchange_info = client.get_exchange_info()
        for symbol in exchange_info['symbols']:
            if symbol['symbol'] == leg1 or symbol['symbol'] == leg2 or symbol['symbol'] == leg3:
                if symbol['status'] != 'TRADING':
                    is_market_closed = True
                    break

        if is_market_closed:
            return

        # Fetch ticker data for all trading pairs
        ticker1 = client.get_symbol_ticker(symbol=leg1)
        ticker2 = client.get_symbol_ticker(symbol=leg2)
        ticker3 = client.get_symbol_ticker(symbol=leg3)

        taker_commission = float(client.get_trade_fee(symbol=leg1)[0]['takerCommission'])
        taker_commission2 = float(client.get_trade_fee(symbol=leg2)[0]['takerCommission'])
        taker_commission3 = float(client.get_trade_fee(symbol=leg3)[0]['takerCommission'])

        # Check if the ticker prices are valid
        if 'price' not in ticker1 or 'price' not in ticker2 or 'price' not in ticker3:
            print(f"Invalid ticker prices for {leg1}, {leg2}, {leg3}.")
            return

        # Extract the ask prices for each leg
        price1_ask = float(ticker1['price'])
        price2_ask = float(ticker2['price'])
        price3_ask = float(ticker3['price'])

        # Calculate the potential profit percentage
        sell_price = price1_ask * (1 - taker_commission)  # Adjust for maker fee
        buy_price = price2_ask * (1 + taker_commission2)  # Adjust for taker fee
        sell_price2 = price3_ask * (1 - taker_commission3)  # Adjust for taker fee

        order_book = client.get_order_book(symbol=leg1)
        q1 = float(order_book['asks'][0][1])
        order_book2 = client.get_order_book(symbol=leg2)
        q2 = float(order_book2['bids'][0][1])
        order_book3 = client.get_order_book(symbol=leg3)
        q3 = float(order_book3['asks'][0][1])

        usdt_balance = 100
        rounded_number1 = math.floor(usdt_balance * calcul(leg1)) / calcul(leg1)

        prof = (((rounded_number1 * sell_price) / buy_price) * sell_price2)
        prof = ((prof / rounded_number1) * 100) - 100
        print(f"Profit percentage for {leg1}, {leg2}, {leg3}: {prof:.2f}%")
        if (rounded_number1 * sell_price) * 1.2 < q1 and ((rounded_number1 * sell_price) / buy_price) * 1.2 < q2:
            print(f"Profit percentage for {leg1}, {leg2}, {leg3}: {prof:.2f}%")

    except Exception as e:
        print(e)
        return


def trade():
    def calcul(symbol):
        # Specify the trading pair symbol
        symbol_info = client.get_symbol_info(symbol)

        # Find the 'LOT_SIZE' filter and extract the minQty value
        min_qty_filter = next(filter(lambda f: f['filterType'] == 'LOT_SIZE', symbol_info['filters']), None)
        if min_qty_filter:
            min_qty = float(min_qty_filter['minQty'])
        else:
            min_qty = 0

        number_string = str(min_qty)
        count = 0

        for digit in number_string:
            if digit == '0':
                count += 1
            elif digit == '.':
                count = 0  # Reset count if decimal point is encountered
            elif digit == '1':
                count += 1
                break

        multipliers = {
            7: 10000000,
            6: 1000000,
            5: 100000,
            4: 10000,
            3: 1000,
            2: 100,
            1: 1,
            0: 1
        }
        return multipliers[count]

    curs = []
    client = Client(api_key, api_secret)
    exchange_info = client.get_exchange_info()
    symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]

    for symbol in exchange_info['symbols']:
        base_currency = symbol['baseAsset']
        quote_currency = symbol['quoteAsset']
        curs.append(base_currency)
        curs.append(quote_currency)

    trading_pairs = []
    x = list(set(curs))

    def generate_currency_legs(currency1, currency2):
        leg1 = f'USDTTRY'  #GBP
        leg2 = f'{currency2}TRY'
        leg3 = f'{currency2}USDT'
        return {
            'leg1': leg1,
            'leg2': leg2,
            'leg3': leg3
        }

    for currency1 in x:
        for currency2 in x:
            if currency1 != currency2:
                try:
                    if generate_currency_legs(currency1, currency2) is None:
                        continue

                    trading_pairs.append(generate_currency_legs(currency1, currency2))
                except:
                    continue

    threads = []

    for pair in trading_pairs:
        t = threading.Thread(target=calculate_profit, args=(pair, client))
        threads.append(t)
        t.start()
        time.sleep(1)

    for t in threads:
        t.join()

trade()
# def shd():
#     try:
#         schedule.every(30).minutes.do(trade)
#         while True:
#             schedule.run_pending()
#
#     except Exception as e:
#         print(e)
#         shd()
#
#
# shd()
