# binance_triangular_arbitrage_bot
The Binance Triangular Arbitrage Repository enables searching profitable pairs, opening market positions, and checking balances in USDT for efficient trading on Binance.


To generate an API for Binance, you can follow these steps:

Visit the Binance website and sign in to your account.
Navigate to the user dashboard or account settings section.
Look for the API Management or API Settings option.
Click on the "Create New API Key" or similar button.
You may be asked to provide additional verification, such as two-factor authentication.
Once verified, you will receive an API key and a secret key. Make sure to keep these keys secure and confidential.
Optionally, you may have the option to set certain restrictions or permissions for your API key, such as enabling only specific trading functions or limiting IP addresses for API access.


The script "find_profitable_combo.py" helps you identify profitable triangular arbitrage opportunities using USDT as a base currency. It scans pairs like leg1 = 'USDTTRY', leg2 = 'currency2TRY', and leg3 = 'currency2USDT' to find potential profitable combinations.
So you start and End with USDT!


The OUTPUT will LIKE:
APIError(code=-1121): Invalid symbol.
APIError(code=-1121): Invalid symbol.
Profit percentage for USDTTRY, SXPTRY, SXPUSDT: -0.33%
Profit percentage for USDTTRY, ANKRTRY, ANKRUSDT: -0.30%
Profit percentage for USDTTRY, UMATRY, UMAUSDT: 0.34%
Profit percentage for USDTTRY, MBOXTRY, MBOXUSDT: 0.31%
...

so take from output those symbols which is mor then 0%


In buildbin.py I paste my profitable pairs like:
texti='''
    Profit percentage for USDTTRY, ANKRTRY, ANKRUSDT: 0.30%
    Profit percentage for USDTTRY, DARTRY, DARUSDT: 0.34%
    Profit percentage for USDTTRY, PORTOTRY, PORTOUSDT: 0.31%
    Profit percentage for USDTTRY, XVSTRY, XVSUSDT: 0.74%
    Profit percentage for USDTTRY, GALTRY, GALUSDT: 0.22%
    Profit percentage for USDTTRY, CITYTRY, CITYUSDT: 0.20%
    Profit percentage for USDTTRY, ENSTRY, ENSUSDT: 0.14%
    ...
    Profit percentage for USDTTRY, OGTRY, OGUSDT: 0.16%N
    Profit percentage for USDTTRY, ZILTRY, ZILUSDT: 0.16%
    Profit percentage for USDTTRY, LINKTRY, LINKUSDT: 0.21%
    Profit percentage for USDTTRY, ETCTRY, ETCUSDT: 0.36%
    Profit percentage for USDTTRY, REEFTRY, REEFUSDT: 0.20%
    Profit percentage for USDTTRY, STXTRY, STXUSDT: 0.40%
    Profit percentage for USDTTRY, RVNTRY, RVNUSDT: 0.42%
    Profit percentage for USDTTRY, COMBOTRY, COMBOUSDT: 0.32%
    Profit percentage for USDTTRY, ACHTRY, ACHUSDT: 0.26%
    '''
I create 5 api key, beacause you have white list limits 30 pair in 1 api, so i paste max pairs in each and use like:
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
buildbin.py balancecheck.py I run at same time to check if ii have real income in genuraly and not just in usdt.
