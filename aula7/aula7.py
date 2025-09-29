'''
exercício para treinamento de POO
projeto cadastrar aluno: sistema para calcular 3 notas de 0 a 10
fazer a médiadas notas, verificar a média do aluno, maior ou
igual a 6 aprovado, menor que 6 reprovado. salvar e armazenar
em uma lista.
'''

'''
Exercício. Refatorar o sistema salvar cadastro em 'alunos.db'
no sqlite, dividir o sistema 'modularizar' e fazer seus devidos
importes.
entregue atividade com sua identificação: data, nome e RA,
entrege o print de banco de dados e seus códigos
devidadmente modularizado, identificado e comentado
'''

class Aluno:
    def __init__(self, nome):
        self.nome=nome
        self.notas=[]
        self.media=0.0
        self.situacao=""
    def adicionar_notas(self):
        for i in range(1,4):
            while True:
                try:
                    nota= float(input(
                        f"Digite a nota {i} entre 0 e 10."))
                    if nota >= 0:
                        if nota <= 10:
                            self.notas.append(nota)
                            break
                    else: print("ERRO nota entre 0 a 10")
                except ValueError: print(
                    "Erro digite uma nota válida!"
                )
    #método para média e situação
    def calcular_media(self):
        self.media=sum(self.notas)/len(self.notas)
        self.situacao="Aprovado" if self.media >= 6 else "Reprovado"
    #método para exibir resultados
    def exibir_dados(self):
        print(f"""
              Nome: {self.nome}
                Notas:{self.notas}
                Média: {self.media}
                Situação: {self.situacao}""")
#class gerencia o cadastro de alunos.
class CadastroAluno:
    def __init__(self):
        self.alunos_=[]
    
    def validar_nome(self):
        while True:
            nome=input("Nome do aluno")
            return nome
    def cadastrar_aluno(self):
        while True:
            nome= self.validar_nome()
            aluno=Aluno(nome)
            aluno.adicionar_notas()
            aluno.calcular_media()
            #armazenar na lista
            self.alunos_.append(aluno)
            continuar=input(
                "'s' para sair ou continuar cadastrando..."
            ). lower()
            if continuar == "s":
                print("Cadastro finalizado...")
                break
    #método exibir todos os alunos
    def exibir_alunos(self):
        for i in self.alunos_:
            i.exibir_dados()

def main():
    print("Cadastro de alunos....")
    sistema=CadastroAluno()
    sistema.cadastrar_aluno()
    sistema.exibir_alunos()
if __name__=="__main__":
    main()