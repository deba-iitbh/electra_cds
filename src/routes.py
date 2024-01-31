from fastapi import APIRouter

from src.controllers.user_controller import users
from src.controllers.product_controller import products
from src.controllers.cart_controller import cart

# main blueprint to be registered with application
api = APIRouter()

api.include_router(users, prefix="/users")
api.include_router(products, prefix="/products")
api.include_router(cart, prefix="/carts")
