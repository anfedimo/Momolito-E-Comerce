from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import schemas
from ..repositories import orders as order_repo, users as user_repo, products as product_repo

def create_order(db: Session, order: schemas.PedidoCreate):
    user = user_repo.get_by_id(db, order.usuario_id)
    product = product_repo.get_by_id(db, order.producto_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no existe.")
    if not product:
        raise HTTPException(status_code=404, detail="Producto no existe.")
    if product.stock < order.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente.")

    product.stock -= order.cantidad
    db.commit()
    return order_repo.create(db, order)

def list_orders(db: Session):
    return order_repo.get_all(db)

def get_order(db: Session, order_id: int):
    order = order_repo.get_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado.")
    return order