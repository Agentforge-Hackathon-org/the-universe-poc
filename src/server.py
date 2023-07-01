import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connected_clients: dict[int, WebSocket] = {}
client_id_counter: int = 0
lock = asyncio.Lock()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global client_id_counter

    await websocket.accept()

    async with lock:
        client_id = client_id_counter
        connected_clients[client_id] = websocket
        client_id_counter += 1

    try:
        while True:
            message = await websocket.receive_text()

            processed_message = f"You sent: {message}"

            await websocket.send_text(processed_message)
    except WebSocketDisconnect:
        async with lock:
            del connected_clients[client_id]

        await websocket.close()


async def broadcast(message: str):
    disconnected_clients = []
    for client_id, client in connected_clients.items():
        try:
            await client.send_text(message)
        except WebSocketDisconnect:
            disconnected_clients.append(client_id)

    if disconnected_clients:
        async with lock:
            for client_id in disconnected_clients:
                del connected_clients[client_id]


@app.post("/broadcast")
async def broadcast_message(message: str):
    await broadcast(message)
    return {"message": "Message broadcasted"}


@app.get("/connected-clients")
async def get_connected_clients():
    return {"connected_clients": len(connected_clients)}
