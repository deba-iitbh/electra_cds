from src.constants import db
from src.models.product_model import Product, category


class ProductManagementActuator:
    def fetch_products(self):
        return Product.query.all()

    def _getProductCategory(self, name):
        if "food" in name.lower():
            return category.food
        elif "clothing" in name.lower():
            return category.clothing
        elif "electronics" in name.lower():
            return category.electronics
        elif "home" in name.lower():
            return category.home
        elif "beauty" in name.lower():
            return category.beauty
        elif "toys" in name.lower():
            return category.toys
        elif "sports" in name.lower():
            return category.sports
        elif "automotive" in name.lower():
            return category.automotive
        else:
            return category.other

    def add_product(self, name, description, price, stock_quantity):
        category = self._getProductCategory(name)
        new_product = Product(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            category=category,
        )
        db.session.add(new_product)
        db.session.commit()
        return True

    def retrieve_product(self, product_id):
        product = Product.query.get(product_id)
        if product:
            return product
        return None

    def update_product(self, product_id, name, description, price, stock_quantity):
        product = Product.query.get(product_id)
        if product:
            if name:
                product.name = name
                product.category = self._getProductCategory(name)
            if description:
                product.description = description
            if price:
                product.price = price
            if stock_quantity:
                product.stock_quantity = stock_quantity
            db.session.commit()
            return True
        return False

    def remove_product(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
