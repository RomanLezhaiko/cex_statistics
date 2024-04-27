import json

import websockets
import requests
import asyncio


class Data(object):
    def __init__(self, binance: dict = None, kucoin: dict = None) -> None:
        self.__binance = binance
        self.__kucoin = kucoin
    

    def get_binance(self):
        return self.__binance
    

    def set_binance(self, binance: dict):
        self.__binance = binance


    def get_kucoin(self):
        return self.__kucoin
    

    def set_kucoin(self, kucoin: dict):
        self.__kucoin = kucoin
    

    def get_info(self):
        if self.__binance is None or self.__kucoin is None:
            return 'Not all data is collected'
        
        return 'Data Kucoin: ' + str(self.__kucoin) + '\nData Binance: ' + str(self.__binance)
    

    def get_arbitrage(self):
        if self.__binance is None or self.__kucoin is None:
            return 'Not all data is collected'
        
        if float(self.__kucoin['bestBid']) < float(self.__binance['a']):
            return 'buy on kucoin, sell on binance  ' + str(float(self.__binance['a']) / float(self.__kucoin['bestBid']))
        
        if float(self.__binance['b']) < float(self.__kucoin['bestAsk']):
            return 'buy on binance, sell on kucoin  ' + str(float(self.__kucoin['bestAsk']) / float(self.__binance['b']))


async def websocket_data(token: str, all_data: Data):
    url_kucoin = f'wss://ws-api.kucoin.com/endpoint?token={token}'
    url_binance = f'wss://fstream.binance.com/ws/bnbusdt@bookTicker'
    
    async with websockets.connect(url_kucoin) as ws_kucoin, websockets.connect(url_binance) as ws_binance:
        while True:
            data_1 = await ws_kucoin.recv()
            res_1 = json.loads(data_1)

            data_2 = await ws_binance.recv()
            res_2 = json.loads(data_2)

            if res_1['type'] == 'welcome':
                data_tmp = {
                    "type": "subscribe",
                    "topic": "/market/ticker:BNB-USDT",
                    "response": True
                }
                json_data = json.dumps(data_tmp)
                await ws_kucoin.send(json_data)
            elif res_1['type'] == 'message':
                # print('Data 1: ---', res_1)
                # print(type(res_1))
                all_data.set_kucoin(res_1['data'])
                # print(all_data.get_info())
                print(all_data.get_arbitrage())
            
            # print('Data 2: ---', res_2)
            all_data.set_binance(res_2)
            # print(all_data.get_info())
            print(all_data.get_arbitrage())


response = requests.post(url='https://api.kucoin.com/api/v1/bullet-public')
data = response.json()
token = data['data']['token']
print(data['data']['token'])
all_data = Data()
asyncio.get_event_loop().run_until_complete(websocket_data(token, all_data))