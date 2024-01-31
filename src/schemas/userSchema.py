from enum import Enum
from pydantic import BaseModel


class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    VENDOR = "VENDOR"
    ADMIN = "ADMIN"


class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    address: str
    role: UserRole

    class config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

    class config:
        orm_mode = True


class UserShow(BaseModel):
    id: int
    username: str
    email: str
    address: str

    class config:
        orm_mode = True
