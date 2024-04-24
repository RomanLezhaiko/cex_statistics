import websockets
import asyncio


async def websocket_data():
    # url = 'wss://stream.binance.com:9443/ws/bnbusdt@depth20@100ms'
    url = 'wss://stream.binance.com:9443/ws/bnbusdt@depth@100ms'
    
    async with websockets.connect(url) as ws:
        while True:
            data = await ws.recv()
            print(data)


asyncio.get_event_loop().run_until_complete(websocket_data())