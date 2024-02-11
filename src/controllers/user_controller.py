from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.schemas.tokenSchema import TokenData
from src.constants import get_db, get_current_user
from src.schemas.userSchema import UserCreate, UserLogin, UserShow, UserRole
from src.services.userService import UserManagementActuator
from src.services.jwtService import jwtActuator


users = APIRouter(tags=["Users"])


@users.post("/register", status_code=status.HTTP_201_CREATED)
def handle_register(data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    Parameters:
    - username: str
    - password: str
    - email: str
    - address: str
    - role: str (Enum: CUSTOMER, VENDOR, ADMIN)

    Returns:
    - Success: 201 OK
    - Failure: 400 Bad Request
    """
    registration_actuator = UserManagementActuator()
    if registration_actuator.create_user(data, db):
        return {"status": "success", "msg": "User registered successfully"}
    else:
        return HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="Failed to register user",
        )


@users.post("/login", status_code=status.HTTP_200_OK)
def handle_login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Authenticate the user and generate a JWT token.

    Parameters:
    - username: str
    - password: str

    Returns:
    - Success: 200 OK with JWT token in cookie
    - Failure: 401 Unauthorized
    """

    authentication_actuator = UserManagementActuator()
    data = UserLogin(username=request.username, password=request.password)
    user = authentication_actuator.authenticate_user(data, db)
    jwtAuth = jwtActuator()

    if user:
        access_token = jwtAuth.create_access_token(
            data={"username": user.username, "role": user.role}
        )
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
        }
    else:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
        )


@users.post("/logout/{user_id}")
def handle_logout(
    user_id: int,
    current_user: TokenData = Depends(get_current_user),
):
    """
    Logs out the user and clears the Cookie

    Returns:
    - Success: 200 OK
    """
    return {"status": "success", "msg": "Logout successful"}


@users.get("/all", status_code=status.HTTP_200_OK)
def get_users(
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    """
    Get the list of users in the system.

    Returns:
        - Success: 200 OK with List of users
        - Failure: 403 Unauthorized
    """
    if current_user.role != UserRole.ADMIN:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this action",
        )

    try:
        userActuator = UserManagementActuator()
        return userActuator.get_all_users(db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
