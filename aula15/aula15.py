from sqlalchemy import create_engine, Column,Integer, String, Float
#create engine = função cria uma instância de forma padrão
#Column = Coluna na tabela do banco de dados
#Integer = tipo int inteiro no banco de dados
#String = str texto é o varchar do database
#float = tipo float real para database
from sqlalchemy.ext.declarative import declarative_base
#sqlalchemy.ext.declarative construtor do objeto para declaração de classes
#produz os objetos do sqlalchemy para mapeamento das tabelas
#declarative_base chamar o mapeamento do orm com base nas
#informações fornecidas
from sqlalchemy.orm import sessionmaker
#sessionmaker configuração de sessão do banco de dados

#criar o engine para conectar ao banco de dados sqlite
engine=create_engine('sqlite:///title.db', echo=True)
#echo vai exibir os comandos do sqlachemy  no terminal
# echo=True para debug
# Base para definir os modelos
Base = declarative_base()
#definir o modelo (equivalente a criar a tabela)
class filme(Base):
    __tablename__ = 'filmes' #nome da tabela no banco
    #atributos do objeto
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    def __repr__(self):
        return f"id={self.id} Nome={self.nome} Ano = {self.ano} Nota= {self.nota}"
def criar_tabela():
    Base.metadata.create_all(engine)#criar a tabela definida
    print("Tabela 'Filmes' criada com sucesso.")
#testar
#criar_tabela()
#criar a sessão (conexão temporária)
def criar_sessao():
    Session = sessionmaker(bind=engine)
    return Session()
#exercicio simples adicionar, visualizar, atualizar e deletar

def inserir_dados():
    sessao= criar_sessao()
    nome = input("Nome do filme: ")
    ano = int(input("Ano do filme: "))
    nota = float(input("Nota do filme: "))
    #instancionar o projeto
    novo_filme = filme(nome=nome, ano=ano, nota=nota)
    sessao.add(novo_filme)
    sessao.commit()
    sessao.close()
    print("Dados adicionais ao banco de dados")

#inserir dados()
#ler os dados no banco
def ler_dados():
    sessao = criar_sessao()
    #consulta com query
    filmes = sessao.query(filme).all()
    #exibir os dados
    for i in filmes:
        print(f"""Dados dos filmes
              ID: {i.id}
              Nome: {i.nome}
              Ano: {i.ano}
              Nota: {i.nota}""")
        sessao.close()

#ler os dados()
#update dos dados
def atualizar_dados():
    sessao = criar_sessao()
    id_filme = int(input("ID do filme para atualizar: "))
    nova_pasta = float(input("Digite a nova nota: "))
    #filtro para a busca
    Filme = sessao.query(filme).filter(filme.id == id_filme).first()
    if Filme:
        Filme.note = nova_pasta
        sessao.commit()
        print("Dados atualizados com sucesso.")
    else: print("Filme não encontrado.")
    sessao.close()
#atualizar_dados()
#inserir_dados()
def deletar_dados():
    sessao = criar_sessao()
    id_filme = int(input("ID do filme para deletar."))
    #consulta para deletar
    filmes = sessao.query(filme).filter(filme.id.in_(id_filme)).all()
    #.in_=iterável qualquer lista[1].....[10]
    if filmes:
        sessao.delete(filmes)
    else: print("Filme não encontrado")
    sessao.commit()
    sessao.close()

def menu():
    while True:
        print("""Operações:
            1- Inserir um filme
            2- Visualizar os filmes
            3- Atualizar um filme
            4- Deletar um filme
            0- Sair
    """)
        op = input("Escolha: ")
        if op == "1": inserir_dados()
        elif op == "2": ler_dados()
        elif op == "3": atualizar_dados()
        elif op == "4": deletar_dados()
        elif op == "0": break
        else: print("opção inválida")

if __name__ == "__main__":
    menu()