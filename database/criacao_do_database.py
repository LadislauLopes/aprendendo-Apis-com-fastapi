from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column

#conecta com o banco e caso não tenha ele cria
engine = create_engine("sqlite:///database/meu_banco.db", echo=True) 

#criando o objetedo do metadata
metadata = MetaData()

usuario = Table(
"usuarios",
metadata, 
Column("id", Integer, primary_key=True,autoincrement=True),
Column("nome",String,nullable=False),
Column("email",String,unique=True,nullable=False),
Column("senha",String,nullable=False)
)
metadata.create_all(engine)

print("Tabelas criadas com sucesso!")