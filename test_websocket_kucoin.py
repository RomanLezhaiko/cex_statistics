import websockets
import requests
import asyncio


# async def websocket_data():
#     # /spotMarket/level2Depth50:BTC-USDT
#     url = 'wss://ws-api.kucoin.com/spotMarket/level2Depth50:BTC-USDT'
    
#     async with websockets.connect(url) as ws:
#         while True:
#             data = await ws.recv()
#             print(data)

response = requests.post(url='https://api.kucoin.com/api/v1/bullet-public')
data = response.json()
print(data['data']['token'])
# asyncio.get_event_loop().run_until_complete(websocket_data())