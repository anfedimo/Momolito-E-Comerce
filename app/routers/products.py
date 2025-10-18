from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..services import products as product_service

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Producto)
def crear_producto(product: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get("/", response_model=list[schemas.Producto])
def listar_productos(db: Session = Depends(get_db)):
    return product_service.list_products(db)

@router.patch("/{product_id}/stock/{stock}", response_model=schemas.Producto)
def actualizar_stock(product_id: int, stock: int, db: Session = Depends(get_db)):
    return product_service.update_stock(db, product_id, stock)