from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: str
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
