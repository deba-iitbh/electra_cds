from pydantic import BaseModel
from src.models.product_model import category


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

    class config:
        orm_mode = True


class ProductShow(ProductCreate):
    id: int
    category: category
