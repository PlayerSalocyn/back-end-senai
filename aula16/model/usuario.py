from aula16.database import *
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__="usuarios"
    id=Column(Integer, primary_key=True,index=True)
    nome=Column(String,index=True)
    email=Column(String,index=True)

#Criar tabelas no banco
Base.metadata.create_all(bind=engine)
