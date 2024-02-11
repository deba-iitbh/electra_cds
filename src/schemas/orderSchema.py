from pydantic import BaseModel
from datetime import datetime
from src.models.order_model import Order,OrderItem


class OrderDetails(BaseModel):
    id: int
    user_id: int
    total: float
    payment_id: int
    class config:
        orm_mode = True


class OrderDetailsShow(OrderDetails):
    id: int
    user_id = int
    total:float
    created_at:datetime
    modified_at:datetime

class OrderItems(BaseModel):
    id: int
    order_id: int
    product_id: int
    class config:
        orm_mode = True


class OrderItemsShow(OrderItems):
    id:int
    product_id:int
    created_at:datetime
    modified_at:datetime


