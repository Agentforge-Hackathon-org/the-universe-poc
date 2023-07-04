from fastapi import FastAPI
from pydantic import BaseModel

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
