from pydantic import BaseModel, Field

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=120)
    email: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=120)
    precio: float = Field(..., ge=0)
    stock: int = Field(..., ge=0)

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    class Config:
        orm_mode = True

class PedidoBase(BaseModel):
    usuario_id: int
    producto_id: int
    cantidad: int = Field(..., ge=1)

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    class Config:
        orm_mode = True
