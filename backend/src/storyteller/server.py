import os

from fastapi import FastAPI
from pydantic import BaseModel

import llm


ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

app = FastAPI()


class ScenePrompt(BaseModel):
    prompt: str


class SceneUpdate(BaseModel):
    current_scene: str
    changes: str


@app.post("/scene")
async def create_scene(prompt: ScenePrompt):
    response = await llm.claude_complete(ANTHROPIC_API_KEY, prompt.prompt)
    return {"scene": response}


@app.put("/scene")
async def update_scene(update: SceneUpdate):
    prompt = f"Here is the current scene: {update.current_scene}.\n" \
             f"Please update the scene given these changes: {update.changes}"
    response = await llm.claude_complete(ANTHROPIC_API_KEY, prompt)
    return {"scene": response}
