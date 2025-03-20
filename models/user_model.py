from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class Usuario(Base):
  __tablename__ = "usuarios"

  id= Column(Integer,primary_key=True,autoincrement=True)
  nome=Column(String,nullable=False)
  email = Column(String,nullable=False)
  senha = Column(String,nullable=False)
  telefone = Column(String,nullable=True)
  def __repr__(self):
    return f"Usuario(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone})"
