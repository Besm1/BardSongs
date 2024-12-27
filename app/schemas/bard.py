from datetime import datetime
from pydantic import BaseModel
'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

from app.backend.db import Base
from sqlalchemy import String, Integer, ForeignKey, Column, Boolean, Date
from sqlalchemy.schema import CreateTable


class Bard(Base):
    __tablename__ = 'bards'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    patronyme = Column(String)
    last_name = Column(String, index=True, nullable=False)
    date_of_birth = Column(Date)
    date_of_death = Column(Date)
    country_of_origin = Column(String)
    city_of_origin = Column(String)
    country_of_residence = Column(String)
    city_of_residence = Column(String)

    class Config:
        orm_mode = True


class CreateBard(BaseModel):
    first_name: str
    patronyme: str
    last_name: str
    date_of_birth: datetime
    date_of_death: datetime
    country_of_origin: str
    city_of_origin: str
    country_of_residence: str
    city_of_residence: str


class UpdateBard(BaseModel):
    id: int
    first_name: str
    patronyme: str
    last_name: str
    date_of_birth: datetime
    date_of_death: datetime
    country_of_origin: str
    city_of_origin: str
    country_of_residence: str
    city_of_residence: str

print(CreateTable(Bard.__table__))