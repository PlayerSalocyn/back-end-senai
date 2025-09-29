"""
Nome: Nycolas Marques
RA: 24271524
Data: 18/08
"""


from aluno import Aluno
from dados import conectar_bd

class CadastroAluno:
    
    def __init__(self):
        self.alunos_=[]
    
    def validar_nome(self):
        while True:
            nome=input("Nome do aluno: ")
            return nome

    def cadastrar_aluno(self):
        while True:
            nome= self.validar_nome()
            aluno=Aluno(nome)
            aluno.adicionar_notas()
            aluno.calcular_media()
            #armazenar na lista
            self.alunos_.append(aluno)

            aluno.exibir_dados()
            continuar=input(
                "'s' para sair ou continuar cadastrando..."
            ). lower()
            if continuar == "s":
                print("Cadastro finalizado...")
                break
    #método exibir todos os alunos
    def exibir_alunos(self):
        conexao, cursor = conectar_bd()
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        conexao.close()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in alunos:
                
                print(f"Nome: {aluno[1]}")
                print(f"Notas: {aluno[2]}")
                print(f"Média: {aluno[3]:.2f}")
                print(f"situação: {aluno[4]}")
                print("-" * 30)