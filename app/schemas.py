from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    pass

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass
