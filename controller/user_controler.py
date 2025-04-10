
from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.user_service import user_create
from schemas.user_schemas import UsuarioSchemas

def create_user(user: UsuarioSchemas, db: Session):
    try:
        
        new_user = user_create(db=db, user=user)
        return new_user
    except Exception as e:
        print('erro controler')
        raise HTTPException(status_code=422, detail=str(e))