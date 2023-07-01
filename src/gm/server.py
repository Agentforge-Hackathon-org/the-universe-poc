from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Scene(BaseModel):
    scene: str


@app.post("/narration")
async def get_narration(scene: Scene):
    return {"narration": "All the people are doing their shit"}
