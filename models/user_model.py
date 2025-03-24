from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base
import uuid
import hashlib
import bcrypt
import os
Base = declarative_base()

# Defina uma chave secreta (Pepper)
SECRET_KEY = os.getenv("SECRET_KEY", "minha_chave_super_secreta").encode()

class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
  nome=Column(String,nullable=False)
  email = Column(String,nullable=False)
  senha = Column(String,nullable=False)
  telefone = Column(String,nullable=True)
  def __repr__(self):
    return f"Usuario(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone})"

  def hash_senha_bcrypt(senha: str) -> str:
    """Gera um hash seguro usando bcrypt e uma chave secreta (peppering)."""
    salt = bcrypt.gensalt()  # Gera um salt aleatório
    senha_peppered = senha.encode() + SECRET_KEY  # Adiciona a SECRET_KEY à senha
    hash_senha = bcrypt.hashpw(senha_peppered, salt)  # Faz o hash com bcrypt
    return hash_senha.decode()  # Retorna o hash como string
  
  def verificar_senha_bcrypt(senha_fornecida: str, hash_armazenado: str) -> bool:
      """Verifica se a senha fornecida corresponde ao hash armazenado usando bcrypt e peppering."""
      senha_fornecida_peppered = senha_fornecida.encode() + SECRET_KEY  # Adiciona o pepper à senha fornecida
      return bcrypt.checkpw(senha_fornecida_peppered, hash_armazenado.encode())  # Verifica o hash