from fastapi import FastAPI

app = FastAPI()


@app.post("/scene")
async def create_scene():
    return {"scene": "People be doin' shit"}


@app.put("/scene")
async def update_shit():
    return {"scene": "People be doin' crazy shit"}
