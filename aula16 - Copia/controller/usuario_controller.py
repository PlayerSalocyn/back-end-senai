#criar usuario e listar
from database import SessionLocal, Usuario
#from model.usuario import Usuario
def criar_usuario(nome:str, email:str):
    session= SessionLocal()
    usuario = Usuario(nome=nome, email=email)
    session.add(usuario)
    session.commit()
    session.close()

def listar_usuarios():
    session=SessionLocal()
    usuarios= session.query(Usuario).all()
    session.close()
    return usuarios

def deletar_usuario(id_usuario:int, novo_nome:str, novo_email:str):
    session=SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.id.in_(id)).all()
    if usuario:
        usuario.nome = novo_nome
        usuario.email = novo_email
        session.commit()
    session.close()
    
def atualizar_usuario(id_usuario:int,
                      novo_nome:str,
                      novo_email:str):
    session = SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if usuario:
        usuario.nome=novo_nome
        usuario.email=novo_email
        session.commit()
    session.close()
