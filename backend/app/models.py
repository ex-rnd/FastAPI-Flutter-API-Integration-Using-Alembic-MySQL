from sqlalchemy import Column, Integer, String, Boolean
# from .database import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    seedless = Column(Boolean, default=True)




