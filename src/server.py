import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

lock = asyncio.Lock()


class ConnectionManager:
    def __init__(self):
        self._connected_clients: set[WebSocket] = set()

    def total_clients(self) -> int:
        return len(self._connected_clients)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        async with lock:
            self._connected_clients.add(websocket)

    async def disconnect(self, websocket: WebSocket):
        async with lock:
            self._connected_clients.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, sender: WebSocket | None = None):
        disconnected_clients = set()

        for client in self._connected_clients:
            # Don't send the message to the sender
            if client != sender:
                try:
                    await client.send_text(message)
                except WebSocketDisconnect:
                    disconnected_clients.add(client)

        if disconnected_clients:
            async with lock:
                for client in disconnected_clients:
                    self._connected_clients.remove(client)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}", sender=websocket)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast(f"{username} has left the chat.")


@app.post("/broadcast")
async def broadcast_message(message: str):
    await manager.broadcast(message)
    return {"message": "Message broadcasted"}


@app.get("/connected-clients")
async def get_connected_clients():
    return {"connected_clients": manager.total_clients()}
