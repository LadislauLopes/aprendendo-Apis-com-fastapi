from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controller.user_controler import user_creator_service , get_user_by_email_controler
from database.conexao_banco import get_db
from schemas.user_schemas import UsuarioSchemas
from models.user_model import Usuario


route = APIRouter(prefix='/user',tags=['Usuario'])

@route.post('/create_user')
def user_creator(user:UsuarioSchemas,db:Session = Depends(get_db)):
    try:
        return user_creator_service(user=user,db=db)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@route.get('/auth')
def login(email: str, passaword:str,db:Session = Depends(get_db) ):
    try:
        user=get_user_by_email_controler(email,db)
        auth = Usuario.verificar_senha_bcrypt(senha_fornecida=passaword,hash_armazenado=user.senha)
    except:
        auth = False
    return auth