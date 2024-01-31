from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.schemas.productSchema import ProductCreate, ProductShow
from src.services.productService import ProductManagementActuator
from src.schemas.userSchema import UserRole
from src.schemas.tokenSchema import TokenData
from src.constants import get_db, get_current_user


# user controller blueprint to be registered with api blueprint
products = APIRouter(tags=["Products"])


@products.post("/", status_code=status.HTTP_201_CREATED)
def handle_create(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Add a new product to the inventory.

    Parameters:
    - name: str
    - description: str
    - price: float
    - stock_quantity: int

    Returns:
    - Success: 200 OK
    - Failure:
        - 403 Unauthorized
        - 417 Bad Request
    """

    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this action",
        )
    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.add_product(data, db):
        return {"status": "success", "msg": "Product added successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to add product",
        )


@products.get("/")
def get_products(
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    fetch the list of products.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        product_management_actuator = ProductManagementActuator()
        return product_management_actuator.fetch_products(db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@products.get("/{pid}")
def get_product(
    pid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    fetch the product with given pid.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        product_management_actuator = ProductManagementActuator()
        product = product_management_actuator.retrieve_product(pid, db)
        if not product:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {pid} does not exist",
            )
        return product

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@products.put("/{pid}", status_code=status.HTTP_201_CREATED)
def update_product(
    pid: int,
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Update an existing product in the inventory.

    Parameters:
    - product_id: int
    - name: str
    - description: str
    - price: float
    - stock_quantity: int

    Returns:
    - Success: 201 OK
    - Failure:
        - 403 Unauthorized
        - 400 Bad Request
    """
    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this action",
        )
    # if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.update_product(pid, data, db):
        return {"msg": "Product updated successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update product",
        )


@products.delete("/{pid}", status_code=status.HTTP_200_OK)
def remove_product(
    pid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Remove a product from the inventory.

    Parameters:
    - product_id: int

    Returns:
    - Success: 200 OK
    - Failure:
        - 403 Unauthorized
        - 400 Bad Request
    """
    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this action",
        )
    # if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.remove_product(pid, db):
        return {"msg": "Product removed successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to remove product",
        )


@products.get("/search?query={query}")
def search_products(
    query: str,
    current_user: TokenData = Depends(get_current_user),
) -> list[ProductShow]:
    """
    Search products in the catalog based on the given query.

    Query Parameters:
    - query: str (search term)

    Returns:
    - Success: 200 OK with list of matching products
    - Failure: 400 Bad Request
    """

    product_management_actuator = ProductManagementActuator()
    matching_products = product_management_actuator.search_products(query)

    return [
        ProductShow(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock_quantity=product.stock_quantity,
            category=product.category,
        )
        for product in matching_products
    ]
