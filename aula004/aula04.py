#aula 04 POO em python

'''
POO = ClassComponentes principais da POO em Python:
classe: define o molde de um objeto(conjunto de atributos
e métodos) -> PascalCase
objeto:é a instância da classe.
atributos:São as características(variáveis) que os objetos da
classe terão
método:são a funções que descrevem o comportamento dos objetos
Herança:Uma classe pode herdar atributos e métodos de outra
classe(chamada de classe pai ou classe base)
Encapsulamento:É um conceito de ocultar detalhes internos de
de um objeto e proteger os dados de acessos externos
Polimosfismo:Diferentes classes podem ter métodos com o mesmo
nome, mas com comportamento diferente.
Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso
'''



#básica de POO em python
class Pessoa:#instância
    def __init__(self,nome):#atributo
        self.nome=nome
    def apresentar(self):#método
        print(f"Olá: {self.nome}")
#consumir o objeto usando uma variavel
nome="james"
#input("Digite o seu nome: ")#input do nome
pessoa=Pessoa(nome)#chamando a instância do objeto
#chamar o método
pessoa.apresentar()

'''
POO: usando um sistema simples de classificar um destino
como viagem.
'''
#class viagem
class Viagem:
    def __init__(self,destino):
        self.destino=destino
#consumir o objeto para criar os destinos
viagem_0=Viagem("Paris")
viagem_1=Viagem("Havaí")
viagem_2=Viagem("Japão")
viagem_3=Viagem("Tailândia")
viagem_4=Viagem("Londres")
#lista os destinos em uma lista
lista_viagem=[viagem_0,viagem_1,viagem_2,viagem_3,
        viagem_4]
#pegar o nome do viajante e os destino escolhido
viajente=input("Digite o seu nome: ")
print(f"{viajente}: temos 5 destinos disponíveis.")
print("""
0-Paris
1-Havaí
2-Japão
3-Tailândia
4-Londres
        """)
selecionado=int(input("Selecione o destino: "))
#acessar o destino pelo índice da lista de 0 a 4
#criar uma variável para armazenar o destino
#destino_selecionado=lista_viagem[selecionado].destino
print(f"{viajente}, seu destino \
{lista_viagem[selecionado].destino} está confirmardo.")