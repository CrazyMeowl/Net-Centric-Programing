import asyncio
import websockets

async def message():
    async with websockets.connect("ws://localhost:8000") as socket:
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())