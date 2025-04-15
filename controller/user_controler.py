
from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from services.user_service import user_creator_service , get_user_by_email_service
from schemas.user_schemas import UsuarioSchemas

def user_creator_controller(user: UsuarioSchemas, db: Session):
    try:
        
        new_user = user_creator_service(db=db, user=user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

def get_user_by_email_controler(email: str, db:Session):
    try:
        user = get_user_by_email_service(email,db=db)
        return user
    except Exception as e:
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca: {e}"
        )