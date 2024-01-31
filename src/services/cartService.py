from sqlalchemy.orm import Session

from src.models.cart_model import CartItem
from src.schemas.cartSchema import Cart


class CartManagementActuator:
    def add_to_cart(self, data: Cart, db):
        existing_item = (
            db.query(CartItem)
            .filter_by(user_id=data.user_id, product_id=data.product_id)
            .first()
        )

        if existing_item:
            existing_item.quantity += data.quantity
        else:
            new_cart_item = CartItem(
                user_id=data.user_id, product_id=data.product_id, quantity=data.quantity
            )
            db.add(new_cart_item)

        db.commit()
        return True

    def remove_from_cart(self, data: Cart, db: Session):
        cart_item = CartItem.query.filter_by(
            user_id=data.user_id, product_id=data.product_id
        ).first()

        if cart_item.quantity <= data.quantity:
            db.delete(cart_item)
        else:
            cart_item.quantity -= data.quantity
        db.commit()
        return True

    def get_all_contents(self, user_id, db: Session):
        cart_items = db.query(CartItem).filter_by(user_id=user_id).all()
        return cart_items
