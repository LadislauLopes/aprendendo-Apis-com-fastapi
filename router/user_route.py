from fastapi import APIRouter, Depends, HTTPException , Response
from sqlalchemy.orm import Session
from controller.user_controler import user_creator_service , get_user_by_email_controler
from database.conexao_banco import get_db
from schemas.user_schemas import UsuarioSchemas
from models.user_model import Usuario
from auth.user_auth import criar_token_acesso

route = APIRouter(prefix='/user',tags=['Usuario'])

@route.post('/create_user')
def user_creator(user:UsuarioSchemas,db:Session = Depends(get_db)):
    try:
        return user_creator_service(user=user,db=db)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@route.get('/auth')
def login(email: str, password: str, db: Session = Depends(get_db), response: Response = Response()):
    try:
        user = get_user_by_email_controler(email, db)
        auth = Usuario.verificar_senha_bcrypt(senha_fornecida=password, hash_armazenado=user.senha)
        
        if not auth:
            raise HTTPException(status_code=401, detail="Senha incorreta")
        
        token = criar_token_acesso(sub=user.id)

        response.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            max_age=1800,  # 30 minutos
            samesite='lax',
            secure=True  # apenas em HTTPS
        )

        return {"mensagem": "Login realizado com sucesso!", "token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Erro na autenticação: {str(e)}")