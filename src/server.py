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

            processed_message = f"Client {client_id} sent: {message}"

            # Broadcast the message to all clients except the sender
            await broadcast(processed_message, sender_id=client_id)
    except WebSocketDisconnect:
        async with lock:
            del connected_clients[client_id]


async def broadcast(message: str, sender_id: int | None):
    disconnected_clients = []
    for client_id, client in connected_clients.items():
        # Don't send the message to the sender
        if client_id != sender_id:
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
    await broadcast(message, sender_id=None)
    return {"message": "Message broadcasted"}


@app.get("/connected-clients")
async def get_connected_clients():
    return {"connected_clients": len(connected_clients)}
