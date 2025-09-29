from sqlalchemy import create_engine, Column,Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

#engine para conectar ao servidor do mariadb
#engine=create_engine('mysql://usuario:senha@localhost:3306/database)
#senha dev1t@24 senha não pode ter @
#senha por dev1t#24
#usuario= dev
#senha = dev1t#24
#pip install mysql-connector pymysql



engine = create_engine('sqlite:///alunos.db',echo=True)
Base = declarative_base()
class Aluno(Base):
    __tablename__="alunos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String,nullable=False)
    nota1 = Column(Float, nullable=False)
    nota2 = Column(Float, nullable=False)
    media = Column(Float, nullable=False)
    situacao= Column(String, nullable=False)
    #retorna os dados em formato de str
    def __repr__(self):
        return f"""Dados dos alunos:
        Nome: {self.nome} Nota1 {self.nota1} Nota2{self.nota2}
        Média: {self.media} Situação: {self.situacao}"""
Base.metabase.create_all(engine)
Session = sessionmaker(bind=engine)

def validar_nome():
    pass
def validar_notas():
    pass
def media():
    pass
def cadastrar_aluno():
    session = Session()
    try:
        nome = input("Nome do aluno")
        notas = float(input("Notas: "))
        media = float(input("média: "))
        situacao = input("Situação ")
        #criar um aluno ao banco de dados
        novo_aluno = Aluno(nome = nome, nota1 = notas, nota2 = notas, media = media, situacao = situacao)
        session.add(novo_aluno)
        session.commit()
        print("Aluno cadastrado.")
    except Exception as erro:
        print(f"Erro ao cadastrar {erro}")
        session.rollback()
    finally:session.close()

def exibir_aluno():
    sessio = Session()
    try:
        alunos = sessio.query(Aluno).all()
        for i in alunos:
            print(f"ID: {i.id} Nome: {i.nome}")
    except Exception as erro:
        print(f"Erro: {erro}")
    finally: sessio.close()

def atualizar():
    exibir_aluno()
    session = Session()
    try:
        id_aluno=int(input(
            "Digite o ID do aluno para atualizar"
        ))
        aluno = session.query(Aluno).filter(Aluno.id==id_aluno).first()
        if aluno:
            #novos dados para atualizar
            nome= input("Digite o nome do aluno: ")
            nota1= float(input("Digite a nota do aluno"))
            nota2= float(input("Digite a nota do aluno"))
            aluno.nome=nome
            aluno.nota1=nota1
            aluno.nota2=nota2
            session.commit()
        else: print("ID não encontrado.")
    except Exception as erro:
        print(f"Erro: {erro}")
        session.rollback
    finally:session.close()
#atualizar()

def deletar_aluno():
    exibir_aluno()
    session = Session()
    try:
        id_aluno=int(input("Id para deletar o aluno: "))
        aluno=session.query(Aluno).filter(Aluno.id==id_aluno).first()
        if aluno:
            session.delete(aluno)
            session.commit()
            print("Aluno deletado.")
        else: print("Id não encontrado.")
    except Exception as erro:
        print(f"Erro: {erro}")
        session.rollback()
    finally:
        session.close()
def menu():
    while True:
        print("""Sistema de gerenciamento de alunos:
              1- Cadastrar
              2- Exibir
              3- Atualizar
              4- Deletar
              0- Sair""")
        op = input("Opção:")
        if op == "1": cadastrar_aluno()
        elif op == "2": exibir_aluno()
        elif op == "3": atualizar()
        elif op == "4": deletar_aluno()
        elif op == "0": break
        else: print("Opção inválida....")

if __name__ == "__name__":
    menu()