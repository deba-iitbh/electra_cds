from src.models.product_model import Product, category
from src.schemas.productSchema import ProductCreate
from src.services.productService import ProductManagementActuator


def test_fetch_products(mock_db):
    # Mocking the data returned by the query
    mock_products = [
        Product(
            id=1,
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock_quantity=5,
            category=category.food,
        ),
        Product(
            id=2,
            name="Product 2",
            description="Description 2",
            price=20.0,
            stock_quantity=10,
            category=category.clothing,
        ),
    ]
    mock_db.query.return_value.all.return_value = mock_products

    actuator = ProductManagementActuator()
    products = actuator.fetch_products(mock_db)
    assert len(products) == 2
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2"


def test_add_product(mock_db):
    data = ProductCreate(
        name="New Product", description="New Description", price=15.0, stock_quantity=8
    )
    actuator = ProductManagementActuator()

    # Mocking the add operation
    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    assert actuator.add_product(data, mock_db) is True


def test_retrieve_product(mock_db):
    product_id = 1
    mock_product = Product(
        id=1,
        name="Product 1",
        description="Description 1",
        price=10.0,
        stock_quantity=5,
        category=category.food,
    )
    mock_db.query.return_value.get.return_value = mock_product

    actuator = ProductManagementActuator()
    product = actuator.retrieve_product(product_id, mock_db)
    assert product.name == "Product 1"


def test_update_product(mock_db):
    product_id = 1
    data = ProductCreate(
        name="Updated Product",
        description="Updated Description",
        price=20.0,
        stock_quantity=15,
    )
    mock_product = Product(
        id=1,
        name="Product 1",
        description="Description 1",
        price=10.0,
        stock_quantity=5,
        category=category.food,
    )
    mock_db.query.return_value.get.return_value = mock_product

    # Mocking the commit operation
    mock_db.commit.return_value = None

    actuator = ProductManagementActuator()
    assert actuator.update_product(product_id, data, mock_db) is True


def test_remove_product(mock_db):
    product_id = 1
    mock_product = Product(
        id=1,
        name="Product 1",
        description="Description 1",
        price=10.0,
        stock_quantity=5,
        category=category.food,
    )
    mock_db.query.return_value.get.return_value = mock_product

    # Mocking the commit operation
    mock_db.commit.return_value = None

    actuator = ProductManagementActuator()
    assert actuator.remove_product(product_id, mock_db) is True


def test_search_product(mock_db):
    name = "Product"
    mock_products = [
        Product(
            id=1,
            name="Product 1",
            description="Description 1",
            price=10.0,
            stock_quantity=5,
            category=category.food,
        ),
        Product(
            id=2,
            name="Product 2",
            description="Description 2",
            price=20.0,
            stock_quantity=10,
            category=category.clothing,
        ),
    ]
    mock_db.query.return_value.filter.return_value.all.return_value = mock_products

    actuator = ProductManagementActuator()
    products = actuator.search_product(name, mock_db)
    assert len(products) == 2
