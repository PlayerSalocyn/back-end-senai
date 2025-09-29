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