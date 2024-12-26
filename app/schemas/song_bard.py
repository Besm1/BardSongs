from datetime import datetime
from pydantic import BaseModel
'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

class Song_Bard(BaseModel):
    id: int
    song_id: int
    bard_id: int
    link_type: int

    class Config:
        orm_mode = True
