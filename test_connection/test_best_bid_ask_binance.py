import websockets
import asyncio


async def websocket_data():
    url = 'wss://fstream.binance.com/ws/bnbusdt@bookTicker'
    
    async with websockets.connect(url) as ws:
        while True:
            data = await ws.recv()
            print(data)


asyncio.get_event_loop().run_until_complete(websocket_data())