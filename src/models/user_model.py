from sqlalchemy import Column, Integer, String, Enum
from src.constants import Base
from src.schemas.userSchema import UserRole


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
