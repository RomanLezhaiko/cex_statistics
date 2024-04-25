import json

import websockets
import requests
import asyncio


async def websocket_data(token: str):
    url = f'wss://ws-api.kucoin.com/endpoint?token={token}'
    
    async with websockets.connect(url) as ws:
        while True:
            data = await ws.recv()
            res = json.loads(data)

            if res['type'] == 'welcome':
                data_tmp = {
                    "type": "subscribe",
                    "topic": "/spotMarket/level2Depth50:ETH-BTC"
                }
                json_data = json.dumps(data_tmp)
                await ws.send(json_data)
            else:
                print(res)


response = requests.post(url='https://api.kucoin.com/api/v1/bullet-public')
data = response.json()
token = data['data']['token']
print(data['data']['token'])
asyncio.get_event_loop().run_until_complete(websocket_data(token))