from fastapi import APIRouter

from src.controllers.user_controller import users
from src.controllers.product_controller import products
from src.controllers.cart_controller import cart
from src.controllers.payment_controller import payment
from src.controllers.order_controller import order

# main blueprint to be registered with application
api = APIRouter()

api.include_router(users, prefix="/users")
api.include_router(products, prefix="/products")
api.include_router(cart, prefix="/carts")
api.include_router(payment, prefix="/payments")
api.include_router(order, prefix="/orders")
