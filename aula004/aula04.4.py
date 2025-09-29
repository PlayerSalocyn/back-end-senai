
'''
Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso
'''
#exemplo simples da Abstração
#abstração precisamos importar um método abstração
from abc import ABC, abstractmethod#conceito de abstração
class Forma:
    #dizer que é uma classe abstrata
    @abstractmethod#chamar o método abstrato
    def area(self):
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
#não a necessidade de chamar a classe pai
retangulo=Retangulo(10,5)#50
circulo=Circulo(7)#153,86
print(f"Área do retângulo é: {retangulo.area()}")
print(f"Área do circulo é: {circulo.area()}")




'''
exercício:POO
criar um sistema em POO para adicionar nome e telefone
de um cliente, e salver em um arquivo .txt e exibir os
clientes
'''