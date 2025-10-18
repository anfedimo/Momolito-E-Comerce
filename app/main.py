from fastapi import FastAPI
from .database import Base, engine
from .routers import users, products, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def read_root():
    return {"status": "ok", "service": "ecommerce", "docs": "/docs"}
