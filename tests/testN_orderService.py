from src.models.order_model import Order, OrderItem
from src.schemas.orderSchema import (
    OrderDetails,
    OrderItems,
)
from src.services.orderService import OrderServiceActuator
from unittest.mock import MagicMock


def test_create_order_items(mock_db):
    data = OrderItems(
        id=1,
        order_id=1,
        product_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    actuator = OrderServiceActuator()

    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    assert actuator.create_order_items(data, mock_db) is True


def test_create_order_details(mock_db):
    data = OrderDetails(
        id=1,
        user_id=1,
        total=100.0,
        payment_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    actuator = OrderServiceActuator()

    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    assert actuator.create_order_details(data, mock_db) is True


def test_get_user_orders(mock_db):
    user_id = 1
    mock_order = Order(
        id=1,
        user_id=1,
        total=100.0,
        payment_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    mock_db.query.return_value.get.return_value = mock_order

    actuator = OrderServiceActuator()
    order = actuator.get_user_orders(user_id, mock_db)
    assert order.id == 1


def test_get_order_by_id(mock_db):
    order_id = 1
    mock_order_item = OrderItem(
        id=1,
        order_id=1,
        product_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    mock_db.query.return_value.get.return_value = mock_order_item

    actuator = OrderServiceActuator()
    order_item = actuator.get_order_by_id(order_id, mock_db)
    assert order_item.id == 1


def test_update_order(mock_db):
    order_id = 1
    data = OrderDetails(
        id=1,
        user_id=1,
        total=200.0,
        payment_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    mock_order = Order(
        id=1,
        user_id=1,
        total=100.0,
        payment_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    mock_db.query.return_value.get.return_value = mock_order
    mock_db.commit.return_value = None

    actuator = OrderServiceActuator()
    assert actuator.update_order(order_id, data, mock_db) is True


def test_delete_order(mock_db):
    order_id = 1
    mock_order = Order(
        id=1,
        user_id=1,
        total=100.0,
        payment_id=1,
        created_at="2024-02-14",
        modified_at="2024-02-14",
    )
    mock_db.query.return_value.get.return_value = mock_order
    mock_db.commit.return_value = None

    actuator = OrderServiceActuator()
    assert actuator.delete_order(order_id, mock_db) is True
