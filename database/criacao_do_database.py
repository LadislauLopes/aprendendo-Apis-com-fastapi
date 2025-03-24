from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
import uuid

def gerar_uuid():
    return str(uuid.uuid4())


#conecta com o banco e caso não tenha ele cria
engine = create_engine("sqlite:///database/meu_banco.db", echo=True) 

#criando o objetedo do metadata
metadata = MetaData()

usuario = Table(
"usuarios",
metadata, 
Column("id", String(36), primary_key=True, unique=True, default=gerar_uuid),
Column("nome",String,nullable=False),
Column("email",String,unique=True,nullable=False),
Column("senha",String,nullable=False),
Column("telefone",String,nullable=True),
)
metadata.create_all(engine)

print("Tabelas criadas com sucesso!")