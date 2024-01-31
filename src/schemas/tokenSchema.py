from pydantic import BaseModel
from typing import Union
from src.schemas.userSchema import UserRole


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    role: Union[str, None] = None
