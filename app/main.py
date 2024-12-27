from fastapi import FastAPI
from routers import bards, songs

app = FastAPI()

@app.get('/')
async def main_get():
    return {'message': 'Песни бардов'}

app.include_router(bards.router)
app.include_router(songs.router)