import requests

response = requests.get('https://api.kucoin.com/api/v1/symbols')
data = response.json()
data_list = data['data']

for item in data_list:
    if 'ETH-BTC' in item['symbol']:
        print(item['symbol'])

# print(response.json())