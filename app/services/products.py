from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import schemas
from ..repositories import products as product_repo

def create_product(db: Session, product: schemas.ProductoCreate):
    return product_repo.create(db, product)

def list_products(db: Session):
    return product_repo.get_all(db)

def update_stock(db: Session, product_id: int, stock: int):
    if stock < 0:
        raise HTTPException(status_code=400, detail="El stock no puede ser negativo.")
    product = product_repo.update_stock(db, product_id, stock)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product