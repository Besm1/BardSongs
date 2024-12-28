from fastapi import APIRouter, HTTPException, Path
# from pydantic.typing import Str, Int, Date
from typing import Annotated

# from ..schemas.bard import Bard, CreateBard
# from ..schemas.song import Song, CreateSong

router = APIRouter(prefix='/songs', tags=['songs'])

songs = []

@router.get('/all')
async def songs_get_all():
    return songs

@router.get('/{title}')
async def songs_get_by_name(title: Annotated[str, Path(..., min_length=2)]):
    b = (b_ for b_ in songs if b_.last_name == title)
    if b:
        return b
    else:
        raise HTTPException(404, detail = f'Песня {title} не найдена')

@router.post('/create/{title}')
async def songs_create(
        title: Annotated[str, Path(...,min_length=2)]
        ):
    pass

@router.put('/update/{ltitle}')
async def songs_update(title: Annotated[str, Path(..., min_length=2)]):
    pass

@router.delete('/delete/{title}')
async def songs_delete(title: Annotated[str, Path(..., min_length=2)]):
    pass
