from src.constants import db, bcrypt
from src.models.user_model import User


class UserRegistrationActuator:
    def register_user(self, username, password, email, address, role):
        new_user = User(
            username=username,
            password=bcrypt.generate_password_hash(password).decode("utf-8"),
            email=email,
            address=address,
            role=role,
        )
        db.session.add(new_user)
        db.session.commit()
        return True


class UserAuthenticationActuator:
    def authenticate_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        return None
