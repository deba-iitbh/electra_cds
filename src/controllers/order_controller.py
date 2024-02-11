from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.schemas.orderSchema import OrderDetails,OrderDetailsShow,OrderItems,OrderItemsShow
from src.services.orderService import OrderServiceActuator
from src.schemas.userSchema import UserRole
from src.schemas.tokenSchema import TokenData
from src.constants import get_db, get_current_user


# user controller blueprint to be registered with api blueprint
order = APIRouter(tags=["Order"])


@order.post("/", status_code=status.HTTP_201_CREATED)
def handle_order_items_create(
    data: OrderItems,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Add a new ordered item.

    Parameters:
    - id:int
    - order_id:int
    - product_id:int
    - created_at:datetime
    - modified_at:datetime

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
    order_management_actuator = OrderServiceActuator()
    if order_management_actuator.create_order_items(data, db):
        return {"status": "success", "msg": "New ordered items added successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to add new ordered items",
        )
@order.post("/", status_code=status.HTTP_201_CREATED)
def handle_order_details_create(
    data: OrderDetails,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Add a new order detail.

    Parameters:
    - id:int
    - user_id:int
    - total:float
    - payment_id:int
    - created_at:datetime
    - modified_at:datetime

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
    order_management_actuator = OrderServiceActuator()
    if order_management_actuator.create_order_details(data, db):
        return {"status": "success", "msg": "New order details added successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to add new order details",
        )
@order.get("/{uid}")
def get_user_order(
    uid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    fetch the order with given user id for a user.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        order_management_actuator = OrderServiceActuator()
        order = order_management_actuator.get_user_orders(uid, db)
        if not order:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order  for user with user_id {uid} does not exist",
            )
        return order

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

@order.get("/{oid}")
def get_order(
    oid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    fetch the order with given oid.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        order_management_actuator = OrderServiceActuator()
        order = order_management_actuator.get_order_by_id(oid, db)
        if not order:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order with id {oid} does not exist",
            )
        return order

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@order.put("/{oid}", status_code=status.HTTP_201_CREATED)
def update_order(
    oid: int,
    data: OrderDetails,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Update an order .

    Parameters:
    -id:int
    -user_id:int
    -total:float
    -payment:int

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
    order_management_actuator = OrderServiceActuator()
    if order_management_actuator.update_order(oid, data, db):
        return {"msg": "Order updated successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update order",
        )


@order.delete("/{oid}", status_code=status.HTTP_200_OK)
def delete_order(
    oid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Delete an order.

    Parameters:
    - order_id: int

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
    order_management_actuator = OrderServiceActuator()
    if order_management_actuator.delete_order(oid, db):
        return {"msg": "Order deleted successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to delete order",
        )
