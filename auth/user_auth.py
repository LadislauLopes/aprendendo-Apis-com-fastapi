from fastapi import status
from jose import jwt, JWTError
from schemas.user_schemas import UsuarioSchemas
from models.user_model import Usuario
from datetime import datetime, timedelta
from pytz import timezone
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse
from jose.exceptions import ExpiredSignatureError, JWTError


load_dotenv()

def _criar_token(tipo_token:str,tempo_vida:timedelta,sub:str):
    """Função que cria e estrutura o token, sub é o id do usuario"""

    payload={}

    fuso_acre = timezone('America/Rio_Branco')
    expira = datetime.now(tz=fuso_acre) + tempo_vida

    payload["type"] = tipo_token
    payload['exp'] = expira
    payload['iat'] = datetime.now(tz=fuso_acre)
    payload['sub'] = sub
    return jwt.encode(payload,os.getenv("JWT_SECRET"),algorithm=os.getenv("ALGORITHM"))

def criar_token_acesso(sub:str):
    """ Função que criar 
        https:/jwt.io
    """
    return _criar_token(
        tipo_token="access_token",
        tempo_vida=timedelta(minutes=30),
        sub=sub
    )

def criar_token_refresh(sub: str):
    return _criar_token(
        tipo_token="refresh_token",
        tempo_vida=timedelta(days=7),  # ou outro tempo desejado
        sub=sub
    )


def gerar_resposta_autenticao(user_id:str):
    """Função que gera a resposta de autenticação com o token"""
    access_token  = criar_token_acesso(sub=user_id)
    refresh_token = criar_token_refresh(sub=user_id)
    response = JSONResponse(content={
        "message": "Login realizado com sucesso!",
        "access_token": access_token ,
        "refresh_token": refresh_token
    })
    response.set_cookie(key='access_token',
                        value=access_token ,
                        httponly=True,
                        max_age=1800,  # 30 minutos
                        samesite='lax',
                        secure=True)  # apenas em HTTPS
    response.set_cookie(key='refresh_token',
                        value=refresh_token,
                        httponly=True,
                        max_age=604800,  # 7 dias
                        samesite='lax',
                        secure=True)  # apenas em HTTPS
    return response

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=[os.getenv("ALGORITHM")])
        return payload.get("sub")
    except ExpiredSignatureError:
        raise ExpiredSignatureError("Token expirado")
    except JWTError:
        return None
