"""
Nome: Nycolas Marques
RA: 24271524
Data: 18/08
"""


from cad_aluno import CadastroAluno

def main():
    print("Cadastro de alunos....")
    sistema=CadastroAluno()
    sistema.cadastrar_aluno()
    sistema.exibir_alunos()

if __name__=="__main__":
    main()




