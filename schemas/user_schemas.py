from pydantic import BaseModel
from typing import Optional

class UsuarioSchemas(BaseModel):
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
