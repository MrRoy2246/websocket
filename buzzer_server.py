import asyncio
import websockets

# Define an empty list to track clients
clients = []
fastest_time = None  # Initialize the fastest_time variable

# Handler function must accept both `websocket` and `path` arguments
async def handle_message(websocket, path):
    global clients
    global fastest_time
    try:
        # Receive the message sent by the client
        message = await websocket.recv()
        if message == "buzz":
            response_time = asyncio.get_event_loop().time()  # Get the response time
            clients.append([websocket, response_time])

            if len(clients) == 1:
                await websocket.send("First place")
                fastest_time = response_time  # Set the fastest time for the first player
            else:
                t = round(response_time - fastest_time, 2)  # Calculate the time difference
                await websocket.send(f"Response time: {t} sec slower")
    except Exception as e:
        print(f"Error in handling message: {e}")

# Start the WebSocket server
async def start_server():
    try:
        # Start the WebSocket server and ensure the handler function is correctly used
        async with websockets.serve(handle_message, "localhost", 8765):
            print("WebSocket server started on ws://localhost:8765")
            await asyncio.Future()  # Keep the server running forever
    except Exception as e:
        print(f"Error starting server: {e}")

# Run the server
if __name__ == "__main__":
    asyncio.run(start_server())
