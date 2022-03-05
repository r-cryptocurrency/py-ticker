import requests

def getcmc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    apikey = 'd3c686b8-d6ab-4c27-8ed9-39e0bd8c254b'
    parameters = {
            'start':'1',
            'limit':'10',

            }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikey,
        }
    session = requests.Session()
    session.headers.update(headers)

    ticker_string = ''
    try:
        r = session.get(url, params=parameters)
        j = r.json()
        with open('cachedCMC.txt', 'w') as f:
            f.write(r.text)
    except:
        print("Failed to get CMC via API")
        with open('cachedCMC.txt', 'r') as f:
            j = f.read().json()
    # for i in j:
    #     print(i)
    return j
