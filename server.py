import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f'server received : {name}')
    greeting = f'Hello {name} !'

    await websocket.send(greeting)
    print(f'server sent : {greeting}')
async def main():
    print("Server start with localhost:8765")
    async with websockets.serve(hello,"localhost",8765):
        await asyncio.Future()

if __name__ =="__main__":
    asyncio.run(main())


