from src.constants import db
from src.models.cart_model import CartItem


class CartManagementActuator:
    def add_to_cart(self, user_id, product_id, quantity):
        existing_item = CartItem.query.filter_by(
            user_id=user_id, product_id=product_id
        ).first()

        if existing_item:
            existing_item.quantity += quantity
        else:
            new_cart_item = CartItem(
                user_id=user_id, product_id=product_id, quantity=quantity
            )
            db.session.add(new_cart_item)

        db.session.commit()
        return True

    def remove_from_cart(self, user_id, product_id):
        cart_item = CartItem.query.filter_by(
            user_id=user_id, product_id=product_id
        ).first()

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return True

        return False
