from datetime import datetime
from pydantic import BaseModel
import enum
from sqlalchemy import Enum
from sqlalchemy import String, Integer, ForeignKey, Column, Boolean, Date, Enum
from sqlalchemy.schema import CreateTable

'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

from app.backend.db import Base
from app.schemas.bard import Bard
from app.schemas.song import Song

'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''


class Role(enum.Enum):
    author = 'автор'
    composer = 'композитор'
    poet = 'поэт'
    singer = 'певец'
    musician = 'музыкант'
    performer = 'исполнитель'
    bard = 'бард'

class Song_Bard(Base):
    __tablename__ = 'song_bard'

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey('songs.id'), nullable=False)
    bard_id = Column(Integer, ForeignKey('bards.id'), nullable=False)
    link_type = Column(Enum(Role))

    class Config:
        orm_mode = True

print(CreateTable(Song_Bard.__table__))