from flask import request, Response, json, Blueprint
from flask_jwt_extended import jwt_required
from src.models.cart_model import CartItem
from src.services.cartService import CartManagementActuator

# user controller blueprint to be registered with api blueprint
cart = Blueprint("cart", __name__)


@cart.route("/", methods=["POST"])
@jwt_required()
def add_to_cart():
    """
    Add an item to the user's cart.

    Parameters:
    - user_id: int
    - product_id: int
    - quantity: int

    Returns:
    - Success: 200 OK
    - Failure: 400 Bad Request
    """
    data = request.get_json()
    try:
        user_id = data["user_id"]
        product_id = data["product_id"]
        quantity = data["quantity"]
    except KeyError:
        return Response(
            response=json.dumps({"status": "failed", "msg": "Missing required fields"}),
            status=400,
            mimetype="application/json",
        )

    cart_management_actuator = CartManagementActuator()
    if cart_management_actuator.add_to_cart(user_id, product_id, quantity):
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Item added to the cart successfully"}
            ),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "failed", "msg": "Failed to add item to the cart"}
            ),
            status=400,
            mimetype="application/json",
        )


@cart.route("/", methods=["DELETE"])
@jwt_required()
def remove_from_cart():
    """
    Remove an item from the user's cart.

    Parameters:
    - user_id: int
    - product_id: int

    Returns:
    - Success: 200 OK
    - Failure: 400 Bad Request
    """
    data = request.get_json()
    try:
        user_id = data["user_id"]
        product_id = data["product_id"]
    except KeyError:
        return Response(
            response=json.dumps({"status": "failed", "msg": "Missing required fields"}),
            status=400,
            mimetype="application/json",
        )

    cart_management_actuator = CartManagementActuator()
    if cart_management_actuator.remove_from_cart(user_id, product_id):
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Item removed from the cart successfully"}
            ),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "failed", "msg": "Failed to remove item from the cart"}
            ),
            status=400,
            mimetype="application/json",
        )


@cart.route("/", methods=["GET"])
@jwt_required()
def get_cart_contents():
    """
    Fetch and return the contents of the user's cart.

    Query Parameters:
    - user_id: int

    Returns:
    - Success: 200 OK with list of cart items
    - Failure: 400 Bad Request
    """
    user_id = request.args.get("user_id")

    if not user_id:
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Missing user_id parameter"}
            ),
            status=400,
            mimetype="application/json",
        )

    # Fetch cart items for the specified user
    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    cart_contents = [
        {"id": item.id, "product_id": item.product_id, "quantity": item.quantity}
        for item in cart_items
    ]

    return Response(
        json.dumps({"status": "success", "items": cart_contents}),
        status=200,
        mimetype="application/json",
    )
