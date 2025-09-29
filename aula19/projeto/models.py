#models.py
from sqlalchemy import Column,Integer,String
#import conexão com sqlite
from database import Base, engine, sessionLocal
#criar o modelo para usuário
class Usuario(Base):
    __tablename__= "usuarios"#nome da tabela
    #Colunas da tabela
    id= Column(Integer, primary_key=True, index=True) #index para o html
    nome= Column(String, index=True)
    email=Column(String, unique=True, index=True)
    #unique para email@plataforma
#teste criar tabela no banco de dados
Base.metadata.create_all(bind=engine)
#função para criar um usuário teste
def criar_user(nome:str,email:str):
    session = sessionLocal()
    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
#criar o user teste
criar_user("User-teste1", "teste1@email.com")