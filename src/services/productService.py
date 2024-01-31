from sqlalchemy.orm import Session

from src.models.product_model import Product, category
from src.schemas.productSchema import ProductCreate, ProductShow


class ProductManagementActuator:
    def fetch_products(self, db: Session):
        return db.query(Product).all()

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

    def add_product(self, data: ProductCreate, db: Session):
        category = self._getProductCategory(data.name)
        new_product = Product(
            name=data.name,
            description=data.description,
            price=data.price,
            stock_quantity=data.stock_quantity,
            category=category,
        )
        try:
            db.add(new_product)
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def retrieve_product(self, product_id: int, db: Session):
        product = db.query(Product).get(product_id)
        if product:
            return ProductShow(**product.__dict__)
        return None

    def update_product(self, pid, data: ProductCreate, db: Session):
        product = db.query(Product).get(pid)
        if product:
            if data.name:
                product.name = data.name
                product.category = self._getProductCategory(product.name)
            if data.description:
                product.description = data.description
            if data.price:
                product.price = data.price
            if data.stock_quantity:
                product.stock_quantity = data.stock_quantity
            try:
                db.commit()
                return True
            except Exception as e:
                print(e)
                db.rollback()
                return False
        return False

    def remove_product(self, product_id, db: Session):
        product = db.query(Product).get(product_id)
        if product:
            db.delete(product)
            db.commit()
            return True
        return False

    def search_product(self, name, db: Session):
        products = (
            db.query(Product)
            .filter(
                Product.name.ilike(f"%{name}%"), Product.description.ilike(f"%{name}%")
            )
            .all()
        )
        if products:
            return products
        return None
