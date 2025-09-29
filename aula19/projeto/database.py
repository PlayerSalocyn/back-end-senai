#database.py
#ordem do padrão mvc
'''
1- definir conexão com banco de dados SQLite -database.py
2- definir o modelo ORM - tabela usuarios , id , nome e email model
3- regras de negócio e rotas do back-end - controller.py
4- template da aplicação view front-end - index.html
5- ponto de saída da aplicação, subir a aplicação main.py
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3
#criar a conexão com o banco de dados sqlite nome database
DATABASE_URL = "sqliter:///./meubanco.db"
# conexao = sqlite3.connect(DATABASE_URL, check_same_thread=)
#engne do banco
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread":False
})
#criar sessão do banco de dados para consultas de usuários
sessionLocal = sessionmaker(bind=engine)
#classe base para os models
Base = declarative_base()