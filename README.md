# Binance Triangular Arbitrage Bot

The Binance Triangular Arbitrage Bot is a tool for efficient trading on the Binance platform. It enables searching for profitable pairs, opening market positions, and checking balances in USDT.

## Generating an API Key for Binance

To generate an API key for Binance, follow these steps:

1. Visit the Binance website and sign in to your account.
2. Navigate to the user dashboard or account settings section.
3. Look for the API Management or API Settings option.
4. Click on the "Create New API Key" or similar button.
5. You may be asked to provide additional verification, such as two-factor authentication.
6. Once verified, you will receive an API key and a secret key. Keep these keys secure and confidential.
7. Optionally, you may have the option to set certain restrictions or permissions for your API key, such as enabling only specific trading functions or limiting IP addresses for API access.

## Identifying Profitable Pairs with `find_profitable_combo.py`

The `find_profitable_combo.py` script helps you identify profitable triangular arbitrage opportunities using USDT as a base currency. It scans pairs like leg1 = 'USDTTRY', leg2 = 'currency2TRY', and leg3 = 'currency2USDT' to find potential profitable combinations. You start and end with USDT.

The output will look like this:

```
APIError(code=-1121): Invalid symbol.
APIError(code=-1121): Invalid symbol.
Profit percentage for USDTTRY, SXPTRY, SXPUSDT: -0.33%
Profit percentage for USDTTRY, ANKRTRY, ANKRUSDT: -0.30%
Profit percentage for USDTTRY, UMATRY, UMAUSDT: 0.34%
Profit percentage for USDTTRY, MBOXTRY, MBOXUSDT: 0.31%
...
```

Choose the symbols with a profit percentage greater than 0%.

## Configuring `buildbin.py`

In `buildbin.py`, paste your profitable pairs like this:

```python
texti = '''
Profit percentage for USDTTRY, ANKRTRY, ANKRUSDT: 0.30%
Profit percentage for USDTTRY, DARTRY, DARUSDT: 0.34%
...
Profit percentage for USDTTRY, ACHTRY, ACHUSDT: 0.26%
'''
```

Create multiple API keys if necessary, as there is a whitelist limit of 30 pairs per API key. Paste the maximum number of pairs for each key and use them like this:

```python
count += 1
if 1 <= count <= 12:
    client = Client(api_key[0], api_secret[0])
elif 13 <= count <= 26:
    client = Client(api_key[1], api_secret[1])
...
elif 55 <= count <= 66:
    client = Client(api_key[4], api_secret[4])
```

Run `buildbin.py` and `balancecheck.py` simultaneously to check if you have real income in general and not just in USDT.

**IMPORTANT:** Use this bot at your own risk. Good luck! If you have any suggestions or improvements, please open an issue and share your ideas for a better implementation of the script.
