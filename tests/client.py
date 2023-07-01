import asyncio
import websockets
import threading


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def send_messages(websocket, loop):
    while True:
        message = await loop.run_in_executor(None, input, "> ")
        await websocket.send(message)


async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"Received from server: {response}")


def start_client(loop):
    uri = "ws://127.0.0.1:8000/ws"

    async def handle_connection():
        async with websockets.connect(uri) as websocket:
            send_task = loop.create_task(send_messages(websocket, loop))
            receive_task = loop.create_task(receive_messages(websocket))
            await asyncio.wait([send_task, receive_task],
                               return_when=asyncio.FIRST_COMPLETED)

    asyncio.run_coroutine_threadsafe(handle_connection(), loop)


if __name__ == "__main__":
    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(new_loop,))
    t.start()

    start_client(new_loop)

    t.join()
