from fastapi import FastAPI, Path, APIRouter

app = FastAPI()

@app.get('/')
async def main_get():
    return {'message': 'Песни бардов'}