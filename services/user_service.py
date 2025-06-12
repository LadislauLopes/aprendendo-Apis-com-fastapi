from schemas.user_schemas import UsuarioSchemas 
from sqlalchemy.orm import Session
from models.user_model import Usuario
from fastapi import HTTPException, status

def user_creator_service(db:Session, user:UsuarioSchemas):
    try:
        hashed_password = Usuario.hash_senha_bcrypt(user.senha)
        new_user = Usuario(nome=user.nome,
                        email=user.email,
                        senha=hashed_password,
                        telefone=user.telefone
                        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Atualiza o objeto 'new_user' com os dados do banco (inclusive o ID)
        return new_user  # Retorna o usuário criado
    except Exception as e:
        
        raise HTTPException(status_code=422, detail=str(e))


def get_user_by_email_service(email: str, db:Session):
    try:
        user = db.query(Usuario).filter(Usuario.email==email).first()
        return user
    except Exception as e:
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca: {e}"
        )
    

