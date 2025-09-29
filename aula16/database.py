from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
#conexao com Saqlite
engine = create_engine("sqlite:///usuario_z.db", echo=True)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

class Usuario(Base):
    __tablename__="usuarios"
    id=Column(Integer, primary_key=True,index=True)
    nome=Column(String,index=True)
    email=Column(String,index=True)

Base.metadata.create_all(bind=engine)
#criar o banco
