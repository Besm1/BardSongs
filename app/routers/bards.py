from fastapi import APIRouter, HTTPException, Path
from typing import Annotated
from datetime import date

# from app.schemas.bard import Bard, CreateBard
from app.schemas.bard import Bard

router = APIRouter(prefix='/bards', tags=['bards'])

bards = []

@router.get('/all')
async def bards_get_all():
    return bards

@router.get('/{last_name}')
async def bards_get_by_name(last_name: Annotated[str, Path(..., min_length=2)]):
    b = (b_ for b_ in bards if b_.last_name == last_name)
    if b:
        return b
    else:
        raise HTTPException(404, detail = f'Бард {last_name} не найден')

@router.post('/create/{last_name}')
async def bards_create(
        first_name: Annotated[str, Path(...,min_length=2)]
        , patronyme: Annotated[str, Path(..., min_length=2)]
        , last_name: Annotated[str, Path(...,min_length=2)]
        , date_of_birth: Annotated[date, Path(...)]
        ):
    global bards
    id_ = max((b_.id for b_ in bards), default=0) + 1
    # bards.append(Bard(id_=id_, ))

@router.put('/update/{last_name}')
async def bards(last_name: Annotated[str, Path(..., min_length=2)]):
    pass

