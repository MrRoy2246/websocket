import asyncio
import websockets
import keyboard

async def start_client():
    try:
        async with websockets.connect("ws://localhost:8765") as websocket:
            done = False
            while not done:
                await asyncio.sleep(0.1)  # Non-blocking sleep to avoid blocking event loop
                if keyboard.is_pressed("space"):
                    await websocket.send("buzz")  # Send "buzz" message when space is pressed
                    message = await websocket.recv()  # Wait for a response from the server
                    print(message)  # Print the server's response
                    done = True  # Exit the loop after receiving the response
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(start_client())
