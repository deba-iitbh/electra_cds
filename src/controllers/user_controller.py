from flask import request, Response, json, Blueprint
from flask_jwt_extended import (
    jwt_required,
    current_user,
    set_access_cookies,
    create_access_token,
    unset_jwt_cookies,
)
from src.models.user_model import User, UserRole
from src.services.userService import (
    UserRegistrationActuator,
    UserAuthenticationActuator,
)
from src.constants import jwt

users = Blueprint("user", __name__)


@jwt.user_lookup_loader
def user_lookup_callback(_, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@users.route("/register", methods=["POST"])
def handle_register():
    """
    Register a new user.

    Parameters:
    - username: str
    - password: str
    - email: str
    - address: str
    - role: str (Enum: CUSTOMER, VENDOR, ADMIN)

    Returns:
    - Success: 200 OK
    - Failure: 400 Bad Request
    """
    data = request.get_json()
    try:
        username = data["username"]
        password = data["password"]
        email = data["email"]
        address = data["address"]
        role = UserRole(data["role"])
    except KeyError:
        return Response(
            response=json.dumps(
                {
                    "status": "failed",
                    "message": "Missing required fields",
                }
            ),
            status=400,
            mimetype="application/json",
        )

    registration_actuator = UserRegistrationActuator()
    if registration_actuator.register_user(username, password, email, address, role):
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "User registered successfully"}
            ),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "failed", "msg": "Error in user registration"}
            ),
            status=400,
            mimetype="application/json",
        )


@users.route("/login", methods=["POST"])
def handle_login():
    """
    Authenticate the user and generate a JWT token.

    Parameters:
    - username: str
    - password: str

    Returns:
    - Success: 200 OK with JWT token in cookie
    - Failure: 401 Unauthorized
    """
    data = request.get_json()
    try:
        username = data["username"]
        password = data["password"]
    except KeyError:
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Missing required fields"}
            ),
            status=400,
            mimetype="application/json",
        )

    authentication_actuator = UserAuthenticationActuator()
    user = authentication_actuator.authenticate_user(username, password)

    if user:
        access_token = create_access_token(identity=user.id)
        response = Response(
            response=json.dumps({"msg": "Login successful"}),
            status=200,
            mimetype="application/json",
        )
        set_access_cookies(response, access_token)
        return response
    else:
        return Response(
            response=json.dumps({"status": "failed", "msg": "Authentication failed"}),
            status=401,
            mimetype="application/json",
        )


@users.route("/logout", methods=["POST"])
def handle_logout():
    """
    Logsout the user and clears the Cookie

    Returns:
    - Success: 200 OK
    """
    response = Response(
        response=json.dumps({"status": "success", "msg": "Logout successful"}),
        status=200,
        mimetype="application/json",
    )
    unset_jwt_cookies(response)
    return response


@users.route("/all", methods=["GET"])
@jwt_required()
def get_users():
    """
    Get the list of users in the system.

    Returns:
        - Success: 200 OK with List of users
        - Failure: 403 Unauthorized
    """
    if current_user.role != UserRole.ADMIN:
        return Response(
            json.dumps(
                {
                    "status": "failed",
                    "msg": "Access denied. You must be an ADMIN to access this resource.",
                }
            ),
            status=403,
            mimetype="application/json",
        )

    users = User.query.all()

    users_data = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role.value,
        }
        for user in users
    ]

    return Response(
        response=json.dumps({"users": users_data}),
        status=200,
        mimetype="application/json",
    )
