from sqlalchemy import Column, Integer, String, Float, DateTime
from src.constants import Base
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime
import importlib

class Order(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey("user.id"), nullable=False)
    total = Column(Float, nullable=False)  # total not calculated
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    # cart = relationship("CartItem")
    # product = relationship("Product")
    @hybrid_property
    def total(self):
        return self.calculate_total()

  # def total(cls):
   #     return select([func.sum(CartItem.product.price * CartItem.quantity)]).where(CartItem.order_id == cls.id).label(
    #        "total")

    def calculate_total(self):
        return sum(item.product.price * item.cart.quantity for item in self.cart)
    #address = relationship("User", back_populates="")
    #orders = relationship("OrderItem", back_populates="items")
    #payment = relationship("Payment", back_populates="payment_details", onclause=payment_id==Payment.id)
    #cart = relationship("CartItem")
    #product = relationship("Product")

    def calculate_total(self):
        return sum(item.product.price * item.cart.quantity for item in self.items)



class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order_details.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    #items=relationship("Order",back_populates="orders")

