from datetime import datetime
from pydantic import BaseModel
'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

class Song(BaseModel):
    id: int
    title: str
    date_of_creation: datetime
    year_of_creation: int
    history: str
    tags: str
    text: str

    class Config:
        orm_mode = True

class CreateSong(BaseModel):
    title: str
    date_of_creation: datetime
    year_of_creation: int
    history: str
    tags: str
    text: str

class UpdateSong(BaseModel):
    id: int
    title: str
    date_of_creation: datetime
    year_of_creation: int
    history: str
    tags: str
    text: str
