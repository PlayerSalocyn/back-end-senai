'''
Nome: Nycolas Marques
RA: 24271524
data: 06/08/2025
Turma: B
'''

lista = {
    "nome": [],
    "numero": []
}

class listar:
    def __init__(self):
        with open("armazem.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                nome = dados[0]
                numero = dados[1]
                
                print(nome, numero)

class contato:
    def __init__(self):
        nome= input("Nome: ")
        num = int(input("número: "))
        self.nome=nome
        self.num=num
    def armazenamento(self):
        with open("armazem.txt", "a") as arquivo:
            arquivo.write(f"{self.nome, self.num}\n")
            lista["nome"].append(self.nome)
            lista["numero"].append(self.num)

    def retornar(self):
        return self.nome, self.num
    

while True:
    print("""1- Adicionar contato
          2- Exibir contatos
          3- sair
""")
    escolha= input("escolha: ")
    if escolha == "1":
        iniciar = contato()
        salvar = iniciar.armazenamento()

        print({iniciar.retornar()})
    elif escolha == "2":
        exibir = listar()
    elif escolha == "3":
        break
    else:
        print("Escolha negada")
