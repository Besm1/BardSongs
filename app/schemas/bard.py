from datetime import datetime
from pydantic import BaseModel
'''
Схемы (schemas) — это структуры данных, которые описывают формат и типы входящих/выходящих данных.
'''

class Bard(BaseModel):
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

