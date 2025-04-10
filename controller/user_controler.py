
from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.user_service import user_creator_service
from schemas.user_schemas import UsuarioSchemas

def user_creator_controller(user: UsuarioSchemas, db: Session):
    try:
        
        new_user = user_creator_service(db=db, user=user)
        return new_user
    except Exception as e:
        print('erro controler')
        raise HTTPException(status_code=422, detail=str(e))