import asyncio
import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import llm

AI21_API_KEY = os.environ.get("AI21_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

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


async def generate_scene(prompt):
    return await llm.claude_complete(ANTHROPIC_API_KEY, prompt)


async def update_scene(scene, changes):
    changes = "\n".join(changes)
    prompt = f"Here is the current scene: {scene}.\n" \
             f"Please update the scene given these changes: {changes}"
    return await llm.claude_complete(ANTHROPIC_API_KEY, prompt)


def get_narration(scene):
    prompt = f"Here is the current scene: {scene}.\n" \
             f"Create some narration to help the characters understand what " \
             f"they need to do."
    return llm.ai21_complete(AI21_API_KEY, prompt)


async def take_action(action):
    prompt = f"The user would like to take the following action: {action}.\n" \
             f"Based on the game rules, what happens next?"
    return await llm.get_narrative_update(OPENAI_API_KEY, prompt)


@app.websocket("/chat/{username}")
async def chat_websocket(websocket: WebSocket, username: str):
    scene_prompt = "Describe a fantasy world"
    scene = ""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # always broadcast message to all players
            await manager.broadcast(f"{username}: {data}", sender=websocket)

            # move on if GM not addressed in message
            if not data.startswith("Hey GM"):
                continue

            # start the game
            if not scene and "start the game" in data:
                scene = await generate_scene(scene_prompt)
                await manager.broadcast(f"Narrator: {get_narration(scene)}")
                continue

            # take an action
            if "I want to" in data:
                result = await take_action(data)
                scene = update_scene(scene, result)
                await manager.broadcast(f"Narrator: {get_narration(scene)}")
                continue

    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast(f"{username} has left the chat.")
