from typing import Optional, List
from sqlalchemy.orm import Session

from src.models.user_model import User
from src.schemas.userSchema import UserCreate, UserLogin, UserShow
from src.services.hashService import Hash


class UserManagementActuator:
    def __init__(self) -> None:
        self.hashActuator = Hash()

    def create_user(self, user: UserCreate, db: Session) -> bool:
        if user.role == "ADMIN":
            return False
        new_user = User(
            username=user.username,
            password=self.hashActuator.get_password_hash(user.password),
            email=user.email,
            address=user.address,
            role=user.role,
        )
        db.add(new_user)
        db.commit()
        return True

    def authenticate_user(self, data: UserLogin, db) -> Optional[User]:
        user = db.query(User).filter(User.username == data.username).first()
        if not user:
            return None
        if not self.hashActuator.verify_password(data.password, user.password):
            return None
        return user

    def get_user(self, user_id, db) -> Optional[User]:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return user
        return None

    def get_all_users(self, db) -> List[Optional[UserShow]]:
        users = db.query(User).all()
        if users:
            return [
                UserShow(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    address=user.address,
                )
                for user in users
            ]
        else:
            return []
