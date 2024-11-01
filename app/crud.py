from sqlalchemy.orm import Session
from . import models, schemas

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Usuario).offset(skip).limit(limit).all()
