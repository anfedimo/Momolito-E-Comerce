from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import schemas
from ..repositories import users as user_repo

def create_user(db: Session, user: schemas.UsuarioCreate):
    existing = user_repo.get_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado.")
    return user_repo.create(db, user)

def list_users(db: Session):
    return user_repo.get_all(db)

def get_user(db: Session, user_id: int):
    user = user_repo.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user