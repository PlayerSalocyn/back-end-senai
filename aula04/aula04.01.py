'''
Sistema gerenciamento de livro.
'''

class Livro:
    def __init__(self,titulo):
        #definir os atributos
        self.titulo=titulo
    #método
    def detalhe(self):
        print(f"título: {self.titulo}")
class Biblioteca:
    def __init__(self):
        self.livro=[]#lista vazia
    #método para add livro a lista
    def add_livro(self,livro):
        self.livro.append(livro) #add a lista
    #def para exibir
    def lista_livros(self):
        print("Livros na biblioteca.")
        #for paa exibir na vertical
        for i in self.livro: #for a lista
            i.detalhe()
    def escolher_livro(self):
        escolha = input("Escolha um livro: ")
        for i in self.livro:
            if escolha == i:
                print("Livro emprestado!")
                break
        print("livro não encontrado")
#criar dois livros
livro1=Livro("O senhor dos anéis")
livro2=Livro("O Hobbit")
livro3=Livro("diário de um banana")
livro4=Livro("A arte da guerra")
livro5=Livro("Bíblia")
livro6=Livro("livro1")
livro7=Livro("livro2")
livro8=Livro("livro3")
livro9=Livro("livro4")
livro10=Livro("livro5")
#adicionar os livros
biblioteca=Biblioteca()
biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)
biblioteca.add_livro(livro3)
biblioteca.add_livro(livro4)
biblioteca.add_livro(livro5)
biblioteca.add_livro(livro6)
biblioteca.add_livro(livro7)
biblioteca.add_livro(livro8)
biblioteca.add_livro(livro9)
biblioteca.add_livro(livro10)
#exibir os livros
biblioteca.lista_livros()
biblioteca.escolher_livro()

'''
Exercício> Sistema biblioteca
(deve criar uma lista com 10 livros:)Pedir o nome do solicitante do empréstimo, pedir para selecionar o livro e imprimir o livro selecionado
'''