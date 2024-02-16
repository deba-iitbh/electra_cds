from pydantic import BaseModel
from datetime import datetime


class OrderDetails(BaseModel):
    user_id: int
    total: float

    class config:
        orm_mode = True


class OrderDetailsShow(OrderDetails):
    user_id: int
    total: float
    created_at: datetime
    modified_at: datetime


class OrderItems(BaseModel):
    id: int
    order_id: int
    product_id: int

    class config:
        orm_mode = True


class OrderItemsShow(OrderItems):
    id: int
    product_id: int
    created_at: datetime
    modified_at: datetime
