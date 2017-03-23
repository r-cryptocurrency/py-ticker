import requests

cmcurl = 'https://api.coinmarketcap.com/v1/ticker?limit=10'

def getcmc():
    ticker_string = ''
    try:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker?limit=10')
        j = r.json()
        with open('cachedCMC.txt', 'w') as f:
            f.write(r.text)
    except:
        print("Failed to get CMC via API")
        with open('cachedCMC.txt', 'r') as f:
            j = f.read().json()
    for i in j:
        ticker_string += "|{}|${}|B{}".format(i['symbol'], i['price_usd'], i['price_btc'])
    return ticker_string
