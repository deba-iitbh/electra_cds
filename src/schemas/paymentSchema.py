from pydantic import BaseModel
from datetime import datetime
from src.models.payment_model import PaymentStatus


class PaymentCreate(BaseModel):
    id: int
    order_id: int
    amount: int
    provider: str

    class config:
        orm_mode = True


class PaymentShow(PaymentCreate):
    id: int
    created_at: datetime
    modified_at: datetime
    status: PaymentStatus
