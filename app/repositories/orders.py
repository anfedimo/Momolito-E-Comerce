from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    return db.query(models.Pedido).all()

def get_by_id(db: Session, order_id: int):
    return db.query(models.Pedido).filter(models.Pedido.id == order_id).first()

def create(db: Session, order: schemas.PedidoCreate):
    db_order = models.Pedido(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order