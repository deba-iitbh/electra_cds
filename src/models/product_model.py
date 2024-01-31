from enum import Enum as enum
from sqlalchemy import Column, Integer, String, Float, Enum
from src.constants import Base


class category(enum):
    food = 1
    clothing = 2
    electronics = 3
    home = 4
    beauty = 5
    toys = 6
    sports = 7
    automotive = 8
    other = 9


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category = Column(Enum(category), nullable=False)
