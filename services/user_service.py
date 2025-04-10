from schemas.user_schemas import UsuarioSchemas 
from sqlalchemy.orm import Session
from models.user_model import Usuario
from fastapi import HTTPException

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
        print(new_user.nome)
        return new_user  # Retorna o usuário criado
    except Exception as e:
        print(e)
        raise HTTPException(status_code=422, detail=str(e))
