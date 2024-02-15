import pytest
from src.services.cartService import CartManagementActuator
from src.models.cart_model import CartItem
from src.schemas.cartSchema import Cart


def test_add_to_cart_existing_item(mock_db):
    # Mocking existing item in the database
    existing_item = CartItem(id=1, user_id=1, product_id=2, quantity=1)
    mock_db.query().filter_by().first.return_value = existing_item

    actuator = CartManagementActuator()
    data = Cart(user_id=1, product_id=2, quantity=2)
    assert actuator.add_to_cart(data, mock_db) is True, "Failed to add to cart"

    # Check that existing item's quantity is increased
    assert existing_item.quantity == 3, "Update qty logic not working"

    # Check that session methods are called appropriately
    mock_db.query().filter_by().first.assert_called_once()
    mock_db.add.assert_not_called()  # No new item added
    mock_db.commit.assert_called_once()


def test_add_to_cart_new_item(mock_db):
    # Mocking non-existing item in the database
    mock_db.query().filter_by().first.return_value = None
    actuator = CartManagementActuator()
    data = Cart(user_id=1, product_id=1, quantity=2)

    assert actuator.add_to_cart(data, mock_db) is True

    # Check that a new item is added
    mock_db.add.assert_called_once()
    new_item = mock_db.add.call_args[0][0]  # Extracting the argument passed to `add`
    assert isinstance(new_item, CartItem)
    assert new_item.user_id == 1
    assert new_item.product_id == 1
    assert new_item.quantity == 2

    # Check that session methods are called appropriately
    mock_db.query().filter_by().first.assert_called_once()
    mock_db.commit.assert_called_once()


def test_remove_from_cart(mock_db):
    # Mocking existing item in the database
    existing_item = CartItem(id=1, user_id=1, product_id=2, quantity=2)
    mock_db.query().filter_by().first.return_value = existing_item

    actuator = CartManagementActuator()

    data = Cart(user_id=1, product_id=1, quantity=1)

    assert actuator.remove_from_cart(data, mock_db) is True

    # Check that existing item's quantity is decreased
    assert existing_item.quantity == 1

    # Check that item is deleted if quantity becomes 0
    data = Cart(user_id=1, product_id=1, quantity=1)
    assert actuator.remove_from_cart(data, mock_db) is True
    mock_db.delete.assert_called_once_with(existing_item)

    # Check that session methods are called appropriately
    mock_db.query().filter_by().first.assert_called()
    mock_db.commit.assert_called()


def test_get_all_contents(mock_db):
    # Mocking cart items in the database
    mock_cart_items = [
        CartItem(quantity=1),
        CartItem(quantity=2),
    ]
    mock_db.query().filter_by().all.return_value = mock_cart_items

    actuator = CartManagementActuator()

    assert actuator.get_all_contents(1, mock_db) == mock_cart_items

    # Check that session methods are called appropriately
    mock_db.query().filter_by().all.assert_called_once()
