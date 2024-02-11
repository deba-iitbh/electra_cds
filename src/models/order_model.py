from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, String, Float, Enum
from src.constants import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Order(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    user_id=Column(String(50),ForeignKey('user.id'),nullable=False)
    total = Column(Float, nullable=False)#total not calculated
    payment_id=Column(Integer,ForeignKey('payment_details.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at=Column(DateTime, default=datetime.utcnow, nullable=False)

    address=relationship("User",back_populates="")
    orders = relationship("OrderItem", back_populates="items")
    payment=relationship("Payment", back_populates="payment_details")
    cart=relationship("CartItem")
    product=relationship("Product")

    def calculate_total(self):
           return sum(item.product.price * item.cart.quantity for item in self.items)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id =Column(Integer, ForeignKey('order_details.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at=Column(DateTime, default=datetime.utcnow, nullable=False)

    items = relationship("Order", back_populates="orders")


