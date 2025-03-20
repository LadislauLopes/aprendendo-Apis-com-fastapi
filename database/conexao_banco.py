from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def conexao_sqlite():
  caminho = os.path.join(os.getcwd(),'meu_banco.db')
  engine = create_engine(f"sqlite:///{caminho}")
  SessionLocal  =sessionmaker(bind=engine)
  return engine, SessionLocal()

