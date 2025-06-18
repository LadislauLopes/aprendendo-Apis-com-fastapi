# Aprendendo APIs com FastAPI

Este projeto é um exemplo prático de como criar uma API RESTful utilizando o framework FastAPI, com autenticação baseada em JWT (access e refresh token), integração com banco de dados SQLite via SQLAlchemy, e estrutura modularizada para facilitar a manutenção e expansão.

## Estrutura do Projeto

```
├── ambiente_virtual.bat           # Script para criar ambiente virtual
├── Criar extrutura base.bat       # Script para criar estrutura base
├── dependencies.py                # Dependências globais do projeto
├── limpa_cache.bat                # Script para limpar cache
├── main.py                        # Arquivo principal para iniciar a aplicação FastAPI
├── meu_banco.db                   # Banco de dados SQLite
├── requirements.txt               # Dependências Python do projeto
├── auth/                          # Lógica de autenticação (JWT, tokens)
│   └── user_auth.py
├── controller/                    # Camada de controle (lógica de negócio)
│   └── user_controler.py
├── database/                      # Conexão e criação do banco de dados
│   ├── conexao_banco.py
│   └── criacao_do_database.py
├── models/                        # Modelos ORM (SQLAlchemy)
│   └── user_model.py
├── router/                        # Rotas da API
│   ├── route_exemple.py
│   └── user_route.py
├── schemas/                       # Schemas Pydantic (validação de dados)
│   └── user_schemas.py
├── services/                      # Serviços auxiliares
│   └── user_service.py
├── utils/                         # Utilitários gerais
└── __pycache__/                   # Arquivos de cache Python
```

## Principais Funcionalidades

- **Cadastro de Usuário**: Endpoint para criar novos usuários.
- **Autenticação**: Login com geração de access token e refresh token (JWT).
- **Refresh Automático**: Renovação automática do access token usando o refresh token.
- **Proteção de Rotas**: Rotas protegidas que exigem autenticação.
- **Validação de Tokens**: Verificação de validade e expiração dos tokens.

## Como Executar

1. **Crie o ambiente virtual:**
   ```powershell
   .\ambiente_virtual.bat
   ```
2. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Inicie a aplicação:**
   ```powershell
   uvicorn main:app --reload
   ```

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints Principais

- `POST /user/create_user` — Criação de usuário
- `GET /user/auth` — Login e geração de tokens
- `GET /user/verify_login` — Verificação e refresh automático de tokens
- `GET /user/teste` — Exemplo de rota protegida

## Observações

- Os tokens são enviados e renovados via cookies HTTPOnly para maior segurança.
- O refresh automático do access token é feito de forma transparente: qualquer rota protegida que dependa de login recebe sempre o user_id válido, sem precisar tratar respostas especiais.
- O projeto utiliza variáveis de ambiente para as chaves JWT (ver `.env`).
- O banco de dados padrão é SQLite, mas pode ser adaptado para outros bancos.

## Requisitos

- Python 3.10+
- FastAPI
- SQLAlchemy
- python-dotenv
- python-jose
- pytz

---

Este projeto serve como base para estudos e pode ser expandido para aplicações reais.
