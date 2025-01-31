from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONM = "sqlite:///projeto2.db"

engine = create_engine(CONM, echo = True)
Session = sessionmaker (bind = engine)
session = Session()
Base = declarative_base()

class Produto (Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

Base.metadata.create_all(engine)