from fastapi import status
from jose import jwt, JWTError
from schemas.user_schemas import UsuarioSchemas
from models.user_model import Usuario
from datetime import datetime, timedelta
from pytz import timezone
from dotenv import load_dotenv
import os
load_dotenv()

def _criar_token(tipo_token:str,tempo_vida:timedelta,sub:str):
    """Função que cria e estrutura o token, sub é o id do usuario"""

    payload={}

    fuso_acre = timezone('America/Rio_Branco')
    expira = datetime.now(fz=fuso_acre) + tempo_vida

    payload["type"] = tipo_token
    payload['exp'] = expira
    payload['iat'] = datetime.now(tz=fuso_acre)
    payload['sub'] = sub
    return jwt.encode(payload,os.getenv("JWT_SECRET"),algorithm=os.getenv("ALGORITHM"))

