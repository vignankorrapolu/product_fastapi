from sqlalchemy.orm import Session
from api.model import Product_Database, Product 

def get_all_products(db:Session):
    return db.query(Product_Database).all()

def get_product_by_id(db:Session,product_id:int):
    return db.query(Product_Database).filter(Product_Database.id ==product_id).first()

def create_product(db: Session, product: Product):
    product_data = product.dict(exclude_unset=True)
    if product_data.get('id') is None:
        product_data.pop('id', None)
    
    db_product = Product_Database(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db:Session,product_id:int,updated_product:Product):
    db_product= db.query(Product_Database).filter(Product_Database.id == product_id).first()
    db_product.name = updated_product.name
    db_product.price = updated_product.price
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product_Database).filter(Product_Database.id == product_id).first()
    if db_product:
        deleted_product = Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price
        )
        db.delete(db_product)
        db.commit()
        return deleted_product
    return None