from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..services import orders as order_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Pedido)
def crear_pedido(order: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, order)

@router.get("/", response_model=list[schemas.Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    return order_service.list_orders(db)

@router.get("/{order_id}", response_model=schemas.Pedido)
def obtener_pedido(order_id: int, db: Session = Depends(get_db)):
    return order_service.get_order(db, order_id)
