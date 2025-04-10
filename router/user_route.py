from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controller.user_controler import create_user
from database.conexao_banco import get_db
from schemas.user_schemas import UsuarioSchemas
route = APIRouter(prefix='/user',tags=['Usuario'])

@route.post('/create_user')
def creater_user(user:UsuarioSchemas,db:Session = Depends(get_db)):
    try:
        return create_user(user=user,db=db)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))