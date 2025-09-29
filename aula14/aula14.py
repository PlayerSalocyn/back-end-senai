#Aula 14 ORM: exemplos básicos de ORM (Mapeamento Objeto-Relacional)'''
'''O ORM SQLAlchemy em Python é uma ferramenta que facilita o
trabalho com bancos de dados relacionais, como SQLite,
MySQL ou PostgreSQL, usando objetos Python em vez de
comandos SQL diretamente.

O que é ORM?
ORM significa Object-Relational Mapping
(Mapeamento Objeto-Relacional).
Ele faz a ponte entre o mundo dos objetos (Python) e o
mundo das tabelas (SQL).
Com ORM, você manipula dados do banco como se fossem objetos
Python, tornando o código mais intuitivo e seguro.

Como funciona o SQLAlchemy ORM?
Modelos: Você define classes Python que representam tabelas do
banco de dados. Cada atributo da classe vira uma coluna da
tabela.
Mapeamento: O SQLAlchemy mapeia essas classes para as tabelas
reais do banco. Sessão: Você usa uma sessão para criar, ler,
atualizar e deletar registros no banco, tudo usando objetos
Python.
Abstração: Não precisa escrever SQL manualmente para operações
básicas; o ORM converte suas ações em comandos SQL.

Vantagens.
Produtividade: Menos código SQL, mais foco na lógica do programa.
Segurança: Evita SQL Injection, pois os dados são tratados
como objetos.
Portabilidade: O mesmo código pode funcionar em diferentes
bancos de dados, mudando apenas a configuração.

Resumindo
O SQLAlchemy ORM permite que você trabalhe com bancos de dados
de forma mais natural em Python, usando classes e objetos,
sem se preocupar com detalhes do SQL.
Isso torna o desenvolvimento mais rápido, seguro e organizado.
'''
#pip install sqlalchemy
#from sqlalchemy import create_engine,Column,Integer,String
#from sqlalchemy.orm import decl_base,sessionmaker
'''
sqlachemy slite3 crud (Create, Read, Update, Delete).

chamadas de importação:
create_engine função cria uma instância de forma padrão para
acessar URL do banco de dados <database_urls> e escreve no
dialeto do sql em forma de string com argumentos de objeto
Column= representa uma coluna no database table
Integer= tipo int inteiro para database table
string=str texto é o varchar do database table

sqlalchemy.orm:
função para configuração do ORM método construtor para mapeamento
do objeto relacional
declarative_base:construtor para declaração de classes
produz os objetos do sqlalchemy para mapeamento de tabelas
chama o orm mapper com base nas informações fornecidas
sessionmaker:configuração de sessão gerar novos objetos
quando chamado com base nos argumentos
session: cria uma sessão para interagir com o banco de dados
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
#Models do paddrão mvc
#cria a base para os modelos ORM
base = declarative_base()
#modelos ORM
#definir o modelo do Usuário
class Usuario(base):
    __tablename__ = "usuarios_"
    id = Column(Integer, primary_key=True)
    nome = Column(String) #nome varchar
    email=Column(String) #email varchar
    #método especial para retornar os dados em texto para terminal
    def __repr__(self):
        #retornar o dados em texto
        return f"<Usuario(id[{self.id}, nome={self.nome}, email={self.email}])>"
#criar banco de dados sqlite e a tabela para inserir os dados
engine = create_engine('sqlite:///usuarios_.db') #criar o arquivo do banco
#criar as tabelas definidas em 'Base'
base.metadata.create_all(engine)#criar a tabela e o id, nome, email
#criar uma sessão para interagir com o banco 'sessionmaker'
Session= sessionmaker(bind=engine) #vincular o engine=cursor
#armazenar a sessão em outra variável
session = Session()
#crud com orm
'''#create - adicionar um usuário
usuario1 = Usuario(nome="Fulano", email= "fulano@email.com")
#add ao banco, chama session
session.add(usuario1)
#salvar e atualizar
session.commit()
'''

usuarios = session.query(Usuario).all()
print("Usuários cadastrados: ")
for i in usuarios:
    print(i)

#update - atualizar um usuário
user_atualizar = session.query(Usuario).filter_by(nome="Fulano").first()#função para retornar as linhas
if user_atualizar:
    user_atualizar.email="fulano@email1234.com"
    session.commit()
    print("Atualizado com sucesso.")
else: print("Usuário não encontrado")
#filter_by criar um filtro em base na igualdade
#first retorna o primeiro resultado da cunsulta
user_deletar=session.query(Usuario).filter_by(nome="Fulano").first()
if user_deletar:
    session.delete(user_deletar)
    session.commit()
    print(f"Usuário deletado. {user_deletar}")
else: print("Usuário não encontrado")