from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.schemas.paymentSchema import PaymentCreate, PaymentShow
from src.services.paymentService import PaymentManagementActuator
from src.schemas.userSchema import UserRole
from src.schemas.tokenSchema import TokenData
from src.constants import get_db, get_current_user


# user controller blueprint to be registered with api blueprint
payment = APIRouter(tags=["Payment"])


@payment.post("/", status_code=status.HTTP_201_CREATED)
def handle_payment_create(
    data: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Add a new payment.

    Parameters:
    - id:int
    - order_id:int
    - amount:int
    - provider:str

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
    payment_management_actuator = PaymentManagementActuator()
    if payment_management_actuator.add_payment(data, db):
        return {"status": "success", "msg": "New Payment added successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to add new payment",
        )


@payment.get("/{pid}", response_model=PaymentShow)
def get_payment(
    pid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    fetch the payment with given pid.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        payment_management_actuator = PaymentManagementActuator()
        payment = payment_management_actuator.get_payment_by_id(pid, db)
        if not payment:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Payment with id {pid} does not exist",
            )
        return payment

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@payment.put("/{pid}", status_code=status.HTTP_201_CREATED)
def update_payment(
    pid: int,
    data: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Update a payment .

    Parameters:
    -id:int
    -order_id:int
    -amount:int
    -provider:str

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
    payment_management_actuator = PaymentManagementActuator()
    if payment_management_actuator.update_payment_status(pid, data, db):
        return {"msg": "Payment updated successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update payment",
        )


@payment.delete("/{pid}", status_code=status.HTTP_200_OK)
def delete_payment(
    pid: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Delete a payment.

    Parameters:
    - payment_id: int

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
    payment_management_actuator = PaymentManagementActuator()
    if payment_management_actuator.delete_payment(pid, db):
        return {"msg": "Payment deleted successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to delete payment",
        )
