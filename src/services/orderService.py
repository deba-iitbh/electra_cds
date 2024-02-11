from sqlalchemy.orm import Session
from src.models.order_model import Order,OrderItem
from src.schemas.orderSchema import OrderDetails,OrderDetailsShow,OrderItems,OrderItemsShow

class OrderServiceActuator:
    def create_order_items(self,data:OrderItems, db:Session):
        new_order_items = OrderItem(
            id=data.id,
            order_id=data.order_id,
            product_id=data.product_id,
            created_at=data.created_at,
            modified_at=data.modified_at
        )
        try:
            db.add(new_order_items)
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def create_order_details(self, data:OrderDetails, db:Session):
        new_order_details = Order(
            id=data.id,
            user_id=data.user_id,
            total=data.total,
            payment_id=data.payment_id,
            created_at=data.created_at,
            modified_at=data.modified_at
        )
        try:
            db.add(new_order_details)
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def get_user_orders(self, user_id:int,db:Session):
        orders = db.query(Order).get(user_id)
        if orders:
            return OrderDetailsShow(**orders.__dict__)
        return None

    def get_order_by_id(self, order_id:int,db:Session):
        order = db.query(OrderItem).get(order_id)
        if order:
            return OrderItemsShow(**order.__dict__)
        return None

    def update_order(self, id,data:OrderDetails,db:Session):
        order = db.query(Order).get(id)
        if order:
            if data.id:
                order.id=data.id
            if data.user_id:
                order.user_id=data.user_id
            if data.total:
                order.total=data.total
            if data.payment_id:
                order.payment=data.payment_id
            try:
                db.commit()
                return True
            except Exception as e:
                print(e)
                db.rollback()
                return False
        return False

    def delete_order(self, order_id,db:Session):
        order = db.query(Order).get(order_id)
        if order:
            db.delete(order)
            db.commit()
            return True
        return False


