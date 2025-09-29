
'''
Polimosfismo:Diferentes classes podem ter métodos com o
mesmo
nome, mas com comportamento diferente.
parecido com herança
polimorfismo com formas de circulo e retangulo
'''
class Forma:#class pai
    #método da classe
    def area(self):#área de uma forma geometrica
        pass
class Retangulo(Forma):#class filho
    #instância para achar a área do retângulo
    def __init__(self,largura,altura):#atributos
        self.largura=largura
        self.altura=altura
    #método para achar a área do retângulo
    def area(self):
        #retornar o resultado da área do retângulo
        return self.largura*self.altura
#subclass filho
class Circulo(Forma):
    def __init__(self,raio):
        self.raio=raio
    #método para área do circulo
    def area(self):
        return 3.14*(self.raio**2)
#chamar a class pai
forna=Forma()#cria a instância
#inputs de  largura e altura
largura=int(input("Entre com a Largura: "))
altura=int(input("Entre com altura: "))
#chamar a classe filho do polimorfismo
retangulo=Retangulo(largura,altura)
print(f"Área do retângulo é: {retangulo.area()}")#retorna o resultado
'''
exercício polimorfismo para achar a área de um circulo
PI=3.14
'''
raio=int(input("Digite o raio do círculo: "))
circulo=Circulo(raio)
#print
print(f"Área do círculo é: {circulo.area()}")