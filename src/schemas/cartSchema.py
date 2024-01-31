from pydantic import BaseModel


class Cart(BaseModel):
    user_id: int
    product_id: int
    quantity: int

    class config:
        orm_mode = True
