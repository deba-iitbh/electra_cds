from xmlrpc.client import DateTime

from sqlalchemy import Column, Integer, String, Float, Enum
from src.constants import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as enum
from datetime import datetime

class PaymentStatus(enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Payment(Base):
    __tablename__ = "payment_details"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer,ForeignKey('order_details.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    provider= Column(String(50), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at=Column(DateTime, default=datetime.utcnow, nullable=False)

    payment_details = relationship("Order", back_populates="payment")

