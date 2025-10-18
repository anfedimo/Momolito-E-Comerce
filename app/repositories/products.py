from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    return db.query(models.Producto).all()

def get_by_id(db: Session, product_id: int):
    return db.query(models.Producto).filter(models.Producto.id == product_id).first()

def create(db: Session, product: schemas.ProductoCreate):
    db_product = models.Producto(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_stock(db: Session, product_id: int, new_stock: int):
    product = get_by_id(db, product_id)
    if product:
        product.stock = new_stock
        db.commit()
        db.refresh(product)
    return product
