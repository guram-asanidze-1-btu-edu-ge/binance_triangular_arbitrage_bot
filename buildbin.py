import time
import threading
import schedule
import math
import keys
from datetime import datetime
import aiohttp
import schedule
from binance.client import Client
def trengular():
    api_key=[keys.api_key1,keys.api_key2,keys.api_key3,keys.api_key4,keys.api_key5]
    api_secret=[keys.secret_key1,keys.secret_key2,keys.secret_key3,keys.secret_key4,keys.secret_key5]
    trading_pairs = []
    count=0
    client = Client(api_key[0], api_secret[0])
    #1-13(1)  14-27(2)  28-41(3)  42-55(4)  56-67(5)
    texti='''
    Profit percentage for USDTTRY, ANKRTRY, ANKRUSDT: 0.30%
    Profit percentage for USDTTRY, DARTRY, DARUSDT: 0.34%
    Profit percentage for USDTTRY, PORTOTRY, PORTOUSDT: 0.31%
    Profit percentage for USDTTRY, XVSTRY, XVSUSDT: 0.74%
    Profit percentage for USDTTRY, GALTRY, GALUSDT: 0.22%
    Profit percentage for USDTTRY, RADTRY, RADUSDT: 0.12%
    Profit percentage for USDTTRY, CITYTRY, CITYUSDT: 0.20%
    Profit percentage for USDTTRY, ENSTRY, ENSUSDT: 0.14%
    Profit percentage for USDTTRY, OGTRY, OGUSDT: 0.16%N
    Profit percentage for USDTTRY, ZILTRY, ZILUSDT: 0.16%
    Profit percentage for USDTTRY, GMTTRY, GMTUSDT: 0.07%
    Profit percentage for USDTTRY, FTMTRY, FTMUSDT: 0.08%
    Profit percentage for USDTTRY, JOETRY, JOEUSDT: 0.21%
    Profit percentage for USDTTRY, MINATRY, MINAUSDT: 0.19%
    Profit percentage for USDTTRY, XTZTRY, XTZUSDT: 0.20%
    Profit percentage for USDTTRY, API3TRY, API3USDT: 0.23%
    Profit percentage for USDTTRY, ALGOTRY, ALGOUSDT: 0.10%
    Profit percentage for USDTTRY, MAGICTRY, MAGICUSDT: 0.13%
    Profit percentage for USDTTRY, FILTRY, FILUSDT: 0.13%
    Profit percentage for USDTTRY, AUDIOTRY, AUDIOUSDT: 0.07%
    Profit percentage for USDTTRY, APETRY, APEUSDT: 0.06%
    Profit percentage for USDTTRY, ONETRY, ONEUSDT: 0.05%
    Profit percentage for USDTTRY, ICPTRY, ICPUSDT: 0.03%
    Profit percentage for USDTTRY, ROSETRY, ROSEUSDT: 0.06%
    Profit percentage for USDTTRY, NEARTRY, NEARUSDT: 0.12%
    Profit percentage for USDTTRY, COSTRY, COSUSDT: 0.13%
    Profit percentage for USDTTRY, AGIXTRY, AGIXUSDT: 0.05%
    Profit percentage for USDTTRY, AXSTRY, AXSUSDT: 0.38%
    Profit percentage for USDTTRY, DENTTRY, DENTUSDT: 0.16%
    Profit percentage for USDTTRY, SUITRY, SUIUSDT: 0.11%
    Profit percentage for USDTTRY, ATOMTRY, ATOMUSDT: 0.08%
    Profit percentage for USDTTRY, OPTRY, OPUSDT: 0.29%
    Profit percentage for USDTTRY, MBOXTRY, MBOXUSDT: 0.31%
    Profit percentage for USDTTRY, ENJTRY, ENJUSDT: 0.19%
    Profit percentage for USDTTRY, SPELLTRY, SPELLUSDT: 0.06%
    Profit percentage for USDTTRY, AVAXTRY, AVAXUSDT: 0.07%
    Profit percentage for USDTTRY, UMATRY, UMAUSDT: 0.34%
    Profit percentage for USDTTRY, CFXTRY, CFXUSDT: 0.07%
    Profit percentage for USDTTRY, TWTTRY, TWTUSDT: 0.23%
    Profit percentage for USDTTRY, SANDTRY, SANDUSDT: 0.42%
    Profit percentage for USDTTRY, RNDRTRY, RNDRUSDT: 0.24%
    Profit percentage for USDTTRY, EDUTRY, EDUUSDT: 0.12%
    Profit percentage for USDTTRY, LTCTRY, LTCUSDT: 0.13%
    Profit percentage for USDTTRY, ONTTRY, ONTUSDT: 0.12%
    Profit percentage for USDTTRY, NEOTRY, NEOUSDT: 0.08%
    Profit percentage for USDTTRY, FETTRY, FETUSDT: 0.41%
    Profit percentage for USDTTRY, MANATRY, MANAUSDT: 0.12%
    Profit percentage for USDTTRY, ALICETRY, ALICEUSDT: 0.14%
    Profit percentage for USDTTRY, LINKTRY, LINKUSDT: 0.21%
    Profit percentage for USDTTRY, XLMTRY, XLMUSDT: 0.12%
    Profit percentage for USDTTRY, ETCTRY, ETCUSDT: 0.36%
    Profit percentage for USDTTRY, TLMTRY, TLMUSDT: 0.08%
    Profit percentage for USDTTRY, VETTRY, VETUSDT: 0.06%
    Profit percentage for USDTTRY, REEFTRY, REEFUSDT: 0.20%
    Profit percentage for USDTTRY, STXTRY, STXUSDT: 0.40%
    Profit percentage for USDTTRY, RVNTRY, RVNUSDT: 0.42%
    Profit percentage for USDTTRY, EOSTRY, EOSUSDT: 0.11%
    Profit percentage for USDTTRY, DOTTRY, DOTUSDT: 0.09%
    Profit percentage for USDTTRY, COMBOTRY, COMBOUSDT: 0.32%
    Profit percentage for USDTTRY, STORJTRY, STORJUSDT: 0.05%
    Profit percentage for USDTTRY, ACHTRY, ACHUSDT: 0.26%
    Profit percentage for USDTTRY, ADATRY, ADAUSDT: 0.14%
    Profit percentage for USDTTRY, BELTRY, BELUSDT: 0.13%
    Profit percentage for USDTTRY, APTTRY, APTUSDT: 0.02%
    Profit percentage for USDTTRY, GRTTRY, GRTUSDT: 0.04%
    Profit percentage for USDTTRY, BSWTRY, BSWUSDT: 0.08%
    '''
    # Split the text into lines
    lines = texti.split('\n')
    for line in lines:
        # Remove leading/trailing whitespaces
        line = line.strip()

        # Check if the line contains the trading pair information
        if line.startswith('Profit percentage for'):
            # Extract the leg1, leg2, and leg3
            legs = line.split(':')[0].replace('Profit percentage for', '').strip().split(',')
            leg1 = legs[0].strip()
            leg2 = legs[1].strip()
            leg3 = legs[2].strip()

            # Create a dictionary for the trading pair
            trading_pair = {
                'leg1': leg1,
                'leg2': leg2,
                'leg3': leg3
            }

            # Append the trading pair to the list
            trading_pairs.append(trading_pair)


    def calcul(symbol):
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
                count = 0
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



    for pair in trading_pairs:
        count+=1
        if 1 <= count <= 12:
            client = Client(api_key[0], api_secret[0])
        elif 13 <= count <= 26:
            client = Client(api_key[1], api_secret[1])
        elif 27 <= count <= 40:
            client = Client(api_key[2], api_secret[2])
        elif 41 <= count <= 54:
            client = Client(api_key[3], api_secret[3])
        elif 55 <= count <= 66:
            client = Client(api_key[4], api_secret[4])
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
                continue

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
                continue

            # Extract the ask prices for each leg
            price1_ask = float(ticker1['price'])
            price2_ask = float(ticker2['price'])
            price3_ask = float(ticker3['price'])

            # Calculate the potential profit percentage
            sell_price = price1_ask * (1 - taker_commission)  # Adjust for maker fee
            buy_price = price2_ask * (1 + taker_commission2)  # Adjust for taker fee
            sell_price2 = price3_ask * (1 - taker_commission3)  # Adjust for taker fee

            order_book = client.get_order_book(symbol=leg1)
            q1 = float(order_book['bids'][0][1])
            order_book2 = client.get_order_book(symbol=leg2)
            q2 = float(order_book2['asks'][0][1])
            order_book3 = client.get_order_book(symbol=leg3)
            q3 = float(order_book3['bids'][0][1])

            usdt_balance = 100
            rounded_number1 = math.floor(usdt_balance * calcul(leg1)) / calcul(leg1)

            prof = (((rounded_number1 * sell_price) / buy_price) * sell_price2)
            prof = ((prof / rounded_number1) * 100) - 100

            print(f"Profit percentage for {leg1}, {leg2}, {leg3}: {prof:.2f}%")
            if prof > 0.4 :
                usdt = leg1[:-3]
                usdt_ball = float(client.get_asset_balance(asset=usdt)['free'])
                rounded = math.floor(usdt_ball * calcul(leg1)) / calcul(leg1)
                if (rounded * sell_price) * 1.2 < q1 and ((rounded * sell_price) / buy_price) * 1.2 < q2 and (((rounded * sell_price) / buy_price) * sell_price2) * 1.2 < q3 :
                    try:
                        usdt = leg1[:-3]
                        usdt_bal = float(client.get_asset_balance(asset=usdt)['free'])
                        print('Start Balance: ', usdt_bal)
                        rounded_numb = math.floor(usdt_bal * calcul(leg1)) / calcul(leg1)
                        order1 = client.create_order(
                            symbol=leg1,
                            side=Client.SIDE_SELL,
                            type=Client.ORDER_TYPE_MARKET,
                            quantity=rounded_numb
                        )
                    except Exception as e:
                        print(e)

                    try:

                        turk = leg1.replace("USDT", "")
                        turk_bal = float(client.get_asset_balance(asset=turk)['free'])
                        rounded_numb2 = math.floor(turk_bal * calcul(leg2)) / calcul(leg2)
                        order2 = client.create_order(
                            symbol=leg2,
                            side=Client.SIDE_BUY,
                            type=Client.ORDER_TYPE_MARKET,
                            quoteOrderQty=rounded_numb2
                        )
                    except Exception as e:
                        print(e)


                    try:
                        turk = leg1.replace("USDT", "")
                        cur = leg2.replace(turk,"")
                        cur_bal = float(client.get_asset_balance(asset=cur)['free'])
                        cur_numb = math.floor(cur_bal * calcul(leg3)) / calcul(leg3)
                        order3 = client.create_order(
                            symbol=leg3,
                            side=Client.SIDE_SELL,
                            type=Client.ORDER_TYPE_MARKET,
                            quantity=cur_numb
                        )
                        usdt = leg1[:-3]
                        usdt_bal = float(client.get_asset_balance(asset=usdt)['free'])
                        print('Finish Balance: ', usdt_bal)
                        current_datetime = datetime.now()
                        print(current_datetime)
                    except Exception as e:
                        print(e)
                else:
                    continue
        except Exception as e:
            print(e)

def shd():
    try:
        schedule.every(1).seconds.do(trengular)
        while True:
            schedule.run_pending()

    except Exception as e:
        print(e)
        shd()

shd()

    # try:
    #
    #     turk = leg1.replace("USDT", "")
    #     turk_bal = float(client.get_asset_balance(asset=turk)['free'])
    #     partry=turk_bal*0.98/buy_price
    #     rounded_numb2 = math.floor(partry * calcul(leg2)) / calcul(leg2)
    #     order2 = client.create_order(
    #         symbol=leg2,
    #         side=Client.SIDE_BUY,
    #         type=Client.ORDER_TYPE_MARKET,
    #         quantity=rounded_numb2
    #     )
    # except Exception as e:
    #     print(e)