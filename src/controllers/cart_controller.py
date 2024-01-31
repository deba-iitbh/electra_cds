from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.schemas.userSchema import UserRole
from src.services.cartService import CartManagementActuator
from src.constants import get_db, get_current_user
from src.schemas.cartSchema import Cart
from src.schemas.tokenSchema import TokenData

cart = APIRouter(tags=["Cart"])


@cart.post("/", status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    data: Cart,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Add an item to the user's cart.

    Parameters:
    - user_id: int
    - product_id: int
    - quantity: int

    Returns:
    - Success: 201 OK
    - Failure: 400 Bad Request
    """
    if current_user.role != UserRole.CUSTOMER:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action",
        )
    cart_management_actuator = CartManagementActuator()
    if cart_management_actuator.add_to_cart(data, db):
        return {"status": "success", "msg": "Item added to the cart successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="Failed to add item to the cart",
        )


@cart.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_cart(
    data: Cart,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Remove an item from the user's cart.

    Parameters:
    - user_id: int
    - product_id: int
    - quantity: int

    Returns:
    - Success: 204 Success
    - Failure: 400 Bad Request
    """
    if current_user.role != UserRole.CUSTOMER:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action",
        )
    cart_management_actuator = CartManagementActuator()
    if cart_management_actuator.remove_from_cart(data, db):
        return {"status": "success", "msg": "Item removed from the cart successfully"}
    else:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Failed to remove item {data.product_id} from cart",
        )


@cart.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=list[Cart])
async def get_cart_contents(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Fetch and return the contents of the user's cart.

    Query Parameters:
    - user_id: int

    Returns:
    - Success: 200 OK with list of cart items
    - Failure: 400 Bad Request
    """
    if current_user.role != UserRole.CUSTOMER:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action",
        )
    # Fetch cart items for the specified user
    cart_management_actuator = CartManagementActuator()
    return cart_management_actuator.get_all_contents(user_id, db)
