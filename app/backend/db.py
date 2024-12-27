from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///bardsongs.db', echo=True)

class Base(DeclarativeBase):
    pass