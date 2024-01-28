from flask import request, Response, json, Blueprint
from flask_jwt_extended import jwt_required, current_user
from src.models.user_model import UserRole
from src.models.product_model import Product
from src.services.productService import ProductManagementActuator
from src.constants import db

# user controller blueprint to be registered with api blueprint
products = Blueprint("product", __name__)


@products.route("/", methods=["POST"])
@jwt_required()
def handle_create():
    """
    Add a new product to the inventory.

    Parameters:
    - name: str
    - description: str
    - price: float
    - stock_quantity: int

    Returns:
    - Success: 200 OK
    - Failure:
        - 403 Unauthorized
        - 400 Bad Request
    """

    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return Response(
            response=json.dumps(
                {
                    "status": "failed",
                    "msg": "Access denied. You must be an VENDOR to access this resource.",
                }
            ),
            status=403,
            mimetype="application/json",
        )
    data = request.get_json()
    try:
        name = data["name"]
        description = data["description"]
        price = data["price"]
        stock_quantity = data["stock_quantity"]
    except KeyError:
        return Response(
            response=json.dumps({"error": "Missing required fields"}),
            status=400,
            mimetype="application/json",
        )

    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.add_product(
        name, description, price, stock_quantity
    ):
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Product added successfully"}
            ),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps({"error": "Failed to add product"}),
            status=400,
            mimetype="application/json",
        )


@products.route("/", methods=["get"])
@jwt_required()
def get_products():
    """
    fetch the list of products.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        product_management_actuator = ProductManagementActuator()
        products = product_management_actuator.fetch_products()
        products_data = [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "stock_quantity": product.stock_quantity,
            }
            for product in products
        ]
        return Response(
            response=json.dumps(products_data),
            status=200,
            mimetype="application/json",
        )
    except exception as e:
        return Response(
            response=json.dumps({"status": "failed", "msg": str(e)}),
            status=500,
            mimetype="application/json",
        )


@products.route("/<pid>", methods=["get"])
@jwt_required()
def get_product(pid):
    """
    fetch the product with given pid.

    returns:
    - success: 200 ok with list of products
    - failure: 500 internal server error
    """
    try:
        product_management_actuator = ProductManagementActuator()
        product = product_management_actuator.retrieve_product(pid)
        if not product:
            return Response(
                response=json.dumps(
                    {
                        "status": "failed",
                        "msg": f"Product with id {pid} does not exist",
                    }
                ),
                status=404,
                mimetype="application/json",
            )
        product_data = {
            "id": pid,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
        }
        return Response(
            response=json.dumps(product_data),
            status=200,
            mimetype="application/json",
        )
    except exception as e:
        return Response(
            response=json.dumps({"status": "failed", "msg": str(e)}),
            status=500,
            mimetype="application/json",
        )


@products.route("/<pid>", methods=["PUT"])
@jwt_required()
def update_product(pid):
    """
    Update an existing product in the inventory.

    Parameters:
    - product_id: int
    - name: str
    - description: str
    - price: float
    - stock_quantity: int

    Returns:
    - Success: 200 OK
    - Failure:
        - 403 Unauthorized
        - 400 Bad Request
    """
    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return Response(
            response=json.dumps(
                {
                    "status": "failed",
                    "msg": "Access denied. You must be an VENDOR to access this resource.",
                }
            ),
            status=403,
            mimetype="application/json",
        )
    data = request.get_json()
    try:
        product_id = pid
        name = data["name"]
        description = data["description"]
        price = data["price"]
        stock_quantity = data["stock_quantity"]
    except KeyError:
        return Response(
            response=json.dumps({"error": "Missing required fields"}),
            status=400,
            mimetype="application/json",
        )

    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.update_product(
        product_id, name, description, price, stock_quantity
    ):
        return Response(
            response=json.dumps({"msg": "Product updated successfully"}),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps({"error": "Failed to update product"}),
            status=400,
            mimetype="application/json",
        )


@products.route("/<pid>", methods=["DELETE"])
@jwt_required()
def remove_product(pid):
    """
    Remove a product from the inventory.

    Parameters:
    - product_id: int

    Returns:
    - Success: 200 OK
    - Failure:
        - 403 Unauthorized
        - 400 Bad Request
    """
    if current_user.role not in [UserRole.VENDOR, UserRole.ADMIN]:
        return Response(
            response=json.dumps(
                {
                    "status": "failed",
                    "msg": "Access denied. You must be an VENDOR to access this resource.",
                }
            ),
            status=403,
            application="application/json",
        )
    try:
        product_id = pid
        assert product_id != None
    except KeyError:
        return Response(
            response=json.dumps({"status": "failed", "msg": "Missing required fields"}),
            status=400,
            mimetype="application/json",
        )

    product_management_actuator = ProductManagementActuator()
    if product_management_actuator.remove_product(product_id):
        return Response(
            response=json.dumps(
                {"status": "success", "msg": "Product removed successfully"}
            ),
            status=200,
            mimetype="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "failed", "msg": "Failed to remove product"}
            ),
            status=400,
            mimetype="application/json",
        )


@products.route("/search", methods=["GET"])
@jwt_required()
def search_products():
    """
    Search products in the catalog based on the given query.

    Query Parameters:
    - query: str (search term)

    Returns:
    - Success: 200 OK with list of matching products
    - Failure: 400 Bad Request
    """
    query = request.args.get("query")

    if not query:
        return Response(
            response=json.dumps({"status": "failed", "msg": "Missing query parameter"}),
            status=400,
            mimetype="application/json",
        )

    # Perform a case-insensitive search on product names and descriptions
    matching_products = Product.query.filter(
        db.or_(
            Product.name.ilike(f"%{query}%"), Product.description.ilike(f"%{query}%")
        )
    ).all()

    products_data = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
        }
        for product in matching_products
    ]

    return Response(
        response=json.dumps(products_data), status=200, mimetype="application/json"
    )
