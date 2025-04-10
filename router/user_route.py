from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controller.user_controler import user_creator_service
from database.conexao_banco import get_db
from schemas.user_schemas import UsuarioSchemas
route = APIRouter(prefix='/user',tags=['Usuario'])

@route.post('/create_user')
def user_creator(user:UsuarioSchemas,db:Session = Depends(get_db)):
    try:
        return user_creator_service(user=user,db=db)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))