from fastapi import APIRouter, HTTPException, Path

from pydantic.typing import Annotated, Str

from app.schemas.bard import Bard, CreateBard

router = APIRouter(prefix='/bards', tags=['bards'])

bards = []

@router.get('/all')
async def all_bards_get():
    return bards

@router.get('/{last_name}')
async def all_bards_get(last_name: str):
    b = (b_ for b_ in bards if b_.last_name == last_name)
    if b:
        return b
    else:
        raise HTTPException(404, detail = f'Бард {last_name} не найден')





