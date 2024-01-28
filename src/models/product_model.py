from enum import Enum
from src.constants import db


class category(Enum):
    food = 1
    clothing = 2
    electronics = 3
    home = 4
    beauty = 5
    toys = 6
    sports = 7
    automotive = 8
    other = 9


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Enum(category), nullable=False)
