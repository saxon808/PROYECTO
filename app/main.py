from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine, Base

# Crea las tablas de la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/", response_model=schemas.UsuarioBase)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, usuario=usuario)

@app.get("/usuarios/", response_model=list[schemas.UsuarioBase])
def leer_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = crud.obtener_usuarios(db, skip=skip, limit=limit)
    return usuarios
