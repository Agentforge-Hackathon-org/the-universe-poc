from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ScenePrompt(BaseModel):
    prompt: str


class SceneUpdate(BaseModel):
    update: str


@app.post("/scene")
async def create_scene(prompt: ScenePrompt):
    return {"scene": "People be doin' shit"}


@app.put("/scene")
async def update_scene(update: SceneUpdate):
    return {"scene": "People be doin' crazy shit"}
