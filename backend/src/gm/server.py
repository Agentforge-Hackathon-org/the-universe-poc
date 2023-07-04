import os

from fastapi import FastAPI
from pydantic import BaseModel

AI21_API_KEY = os.environ.get("AI21_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = FastAPI()


class Scene(BaseModel):
    scene: str


class Action(BaseModel):
    character: str
    action: str


@app.post("/narrative")
async def get_narration(scene: Scene):
    return {"narrative": "All the people are doing their shit"}


@app.post("/evaluate")
async def evaluate_action(action: Action):
    return {"result": "This guy did some shit"}
