from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Column, Boolean, Date
from sqlalchemy.schema import CreateTable

from app.backend.db import Base

'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date_of_creation = Column(Date)
    year_of_creation = Column(Integer)
    history = Column(String)
    tags = Column(String)
    text = Column(String)

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

print(CreateTable(Song.__table__))