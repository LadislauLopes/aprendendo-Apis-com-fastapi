from fastapi import APIRouter, Depends, HTTPException ,Request
from sqlalchemy.orm import Session
from controller.user_controler import user_creator_service , get_user_by_email_controler
from database.conexao_banco import get_db
from schemas.user_schemas import UsuarioSchemas
from models.user_model import Usuario
from auth.user_auth import gerar_resposta_autenticao , verificar_token
from jose.exceptions import ExpiredSignatureError, JWTError
route = APIRouter(prefix='/user',tags=['Usuario'])

@route.post('/create_user')
def user_creator(user:UsuarioSchemas,db:Session = Depends(get_db)):
    try:
        return user_creator_service(user=user,db=db)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    

@route.get('/auth')
def login(email: str, password: str, db: Session = Depends(get_db)):
    try:
        user = get_user_by_email_controler(email, db)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        auth = Usuario.verificar_senha_bcrypt(senha_fornecida=password, hash_armazenado=user.senha)

        if not auth:
            raise HTTPException(status_code=401, detail="Senha incorreta")

        return gerar_resposta_autenticao(user_id=user.id)

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Erro na autenticação: {str(e)}")




@route.get('/verify_login')
def verify_login(request: Request):
    access_token = request.cookies.get('access_token')
    refresh_token = request.cookies.get('refresh_token')

    if not access_token or not refresh_token:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")

    try:
        # Primeiro tenta validar o access token
        user_id = verificar_token(access_token)
        if user_id:
            return {"mensagem": "Usuário autenticado", "user_id": user_id}

    except ExpiredSignatureError:
        # Access token expirou — tenta validar o refresh
        try:
            user_id = verificar_token(refresh_token)
            if not user_id:
                raise HTTPException(status_code=401, detail="Refresh token inválido")

            # Gera novo access token e atualiza o cookie

            return gerar_resposta_autenticao(user_id=user_id)

        except JWTError:
            raise HTTPException(status_code=401, detail="Refresh token inválido")

    except JWTError:
        raise HTTPException(status_code=401, detail="Access token inválido")

    # Fallback
    raise HTTPException(status_code=401, detail="Erro ao validar tokens")


@route.get('/teste')
def rota_protegida(user_id: str = Depends(verify_login)):
    return {"message": "Alo mundo", "user_id": user_id}