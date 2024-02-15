from unittest.mock import MagicMock
from src.models.user_model import User
from src.schemas.userSchema import UserRole as Role
from src.schemas.userSchema import UserCreate, UserLogin
from src.services.userService import UserManagementActuator


def test_create_user(mock_db):
    user_actuator = UserManagementActuator()
    user_create_data = UserCreate(
        username="test_user",
        password="test_password",
        email="test@example.com",
        address="123 Test St",
        role=Role.CUSTOMER,
    )
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    result = user_actuator.create_user(user_create_data, mock_db)
    assert result == True
    mock_db.add.assert_called_once()


def test_create_user_admin_role():
    user_actuator = UserManagementActuator()
    user_create_data = UserCreate(
        username="admin_user",
        password="admin_password",
        email="admin@example.com",
        address="123 Admin St",
        role=Role.ADMIN,
    )
    mock_db = MagicMock()
    result = user_actuator.create_user(user_create_data, mock_db)
    assert result == False


def test_authenticate_user_valid_credentials():
    user_actuator = UserManagementActuator()
    user_login_data = UserLogin(username="test_user", password="test_password")
    user = User(
        username="test_user",
        password=user_actuator.hashActuator.get_password_hash("test_password"),
        email="test@example.com",
        address="123 Test St",
        role="USER",
    )
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = user
    result = user_actuator.authenticate_user(user_login_data, mock_db)
    assert result == user


def test_authenticate_user_invalid_username():
    user_actuator = UserManagementActuator()
    user_login_data = UserLogin(username="non_existing_user", password="test_password")
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    result = user_actuator.authenticate_user(user_login_data, mock_db)
    assert result == None


def test_authenticate_user_invalid_password():
    user_actuator = UserManagementActuator()
    user_login_data = UserLogin(username="test_user", password="wrong_password")
    user = User(
        username="test_user",
        password=user_actuator.hashActuator.get_password_hash("test_password"),
        email="test@example.com",
        address="123 Test St",
        role="USER",
    )
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = user
    result = user_actuator.authenticate_user(user_login_data, mock_db)
    assert result == None


def test_get_user_valid_id():
    user_actuator = UserManagementActuator()
    user_id = 1
    user = User(
        id=1,
        username="test_user",
        email="test@example.com",
        address="123 Test St",
        role="USER",
    )
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = user
    result = user_actuator.get_user(user_id, mock_db)
    assert result == user


def test_get_user_invalid_id():
    user_actuator = UserManagementActuator()
    user_id = 999
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    result = user_actuator.get_user(user_id, mock_db)
    assert result == None


def test_get_all_users():
    user_actuator = UserManagementActuator()
    users = [
        User(id=1, username="user1", email="user1@example.com", address="123 User St"),
        User(id=2, username="user2", email="user2@example.com", address="456 User St"),
    ]
    mock_db = MagicMock()
    mock_db.query.return_value.all.return_value = users
    result = user_actuator.get_all_users(mock_db)
    assert len(result) == 2
