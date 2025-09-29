#models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base, engine, SessionLocal

#tabela de produtos
class Produto(Base):
    __tablename__="produtos"
    id = Column(Integer)
    nome = Column(String, nullable=False, index=True)
    preco= Column(Float, nullable=False)
    quantidade= Column(Integer, nullable=False)
    imagem= Column(String, nullable=True)
#criar banco e tabelas
Base.metadata.create_all(bind=engine)

nome="camisa"
preco=89.55
quantidade=10
imagem="sem foto"
novo=Produto(nome=nome,preco=preco,quantidade=quantidade, imagem=imagem)

db=SessionLocal()
db.add(novo)
db.commit()