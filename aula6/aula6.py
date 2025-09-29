class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#Chamada de método
pessoa = Pessoa("Fulano", 20)
print(pessoa.nome,pessoa.idade)
'''
Método especial para string __str__ e __repr__
__str__ retorna uma string mais legível do objeto (para o usuário)
__repr__ retorna uma string mais técnica do objeto (para dev)
'''

class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    #método especial para retornar uma string do objeto
    def __str__(self):
        return f"Livro: {self.titulo} Autor:{self.autor}"
    #método especial para retornar uma string do objeto mais técnica
    def __repr__(self):
        return f"Livro: {self.titulo} Autor: {self.autor}"
    #método especial para retornar uma string do objeto mais técnica
    def __repr__(self):
        return F"Livro: {self.titulo}' Autor: '{self.autor}'"
livro = Livro("O Hobbit", "J.R.R Tolkien")
#método de str e repr
print(str(livro))
print(repr(livro))
'''
método __len__ tamanho do objeto = a função len()
'''
class Playlist:
    def __init__(self, musicas):
        self.musicas=musicas
    def __len__(self):
        return len(self.musicas)
#chamada do objeto
playlist = Playlist(["musicao1","musica2","musica3","musica4"])
#quantidade de músicas na playlist
print(len(playlist)) #4
'''
Métodos especiais para operações matemáticas
__add__=soma, __sub__=subtração, __mul__= multiplicação,
__truediv__=divisao
(+,-,*,/)
'''
class Operacao:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self,num):
        return Operacao(self.x+num.x, self.y+num.y)
    def __str__(self):
        return f"Operação({self.x},{self.y})"
#criar os números
p1= Operacao(1,2)
p2=Operacao(3,4)
soma=p1+p2
print(soma)
'''
chamada do p1.__(p2) saída: Operação (4,6)
'''
'''
Comparação de objetos: __eq__ __lt__ comparação como ==,<,>
'''
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def __eq__(self,numero):
        return self.nota == numero.nota
    def __lt__(self, numero):
        return self.nota < numero.nota
#criar dois alunos e comprar as notas
aluno1=Aluno("fulano", 8.5)
aluno2=Aluno("Ciclano", 7.0)
print(aluno1 == aluno2) #false
print(aluno1 < aluno2) #false
'''
método para acessar elementos do objeto.
__gettem__ e __setitem__ permite acessar com o get e modificar
com set usando o objeto[chave]= parecido com dicionários
'''

class ListaPersonalizada:
    def __init__(self, elementos):
        self.elementos = elementos
    def __getitem__(self,indice):
        self.elementos[indice]
    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor
#criar uma lista
lista = ListaPersonalizada([10,20,30,40,50])
#acessar
print(lista[0])#saída 10
#modificar
lista[1]=99
print(lista[1]) #99

'''
__call__ torna um objeto chamável permitindo que o objeto seja
chamado como uma função
'''
class Multiplicar:
    def __init__(self, numero):
        self.numero=numero
    def __call__(self, x):
        return x*self.numero
#chamar o objeto
dobro= Multiplicar(2)
print(dobro(5))#10
'''
quando usar métodos especiais?
quando você quer o objeto se comporte como uma lista ou
dicionário

para definir representação string como __str__
para definir operadores(+,-) __add__
para definir comparação ==,<,> __eq__
'''
'''
exercício para treinamento de POO
projeto cadastrar aluno: sistema para calcular 3 notas de 0 a 10
fazer a médiadas notas, verificar a média do aluno, maior ou
igual a 6 aprovado, menor que 6 reprovado. salvar e armazenar
em uma lista.
'''
