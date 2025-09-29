#Aula02
#Revisão da aula 01

'''
recapitulação de função...
mini crud(Create, Read, Update, Delete)
sistema do aluno, cadastrar aluno e notas
verificar se está aprovado ou reprovado
'''


#1°função validar o nome do aluno
def validar_nome():
    while True:
        nome=input("Digite o nome.")
        if len(nome)>=5:
            return nome
        else:
            print("Nome inválido.")
#2°função validar as notas
def validar_notas():
    notas=[]
    for i in range(1,3):
        while True:
            nota=float(input(
        f"Digite a nota {i}:"))
            if nota <=0 or nota <=10:
                notas.append(nota)
                break
            else:print("Nota inválida")
    return notas
#3°função média
def calcular_media(notas):
    media=sum(notas)/len(notas)
    situacao="aprovado" if media >=6 else "Reprovado"
    return media,situacao
#4°função cadastro
def cadastro_alunos():
    alunos=[]
    nome=validar_nome()
    notas=validar_notas()
    media,situacao=calcular_media(notas)
    alunos.append({
        "nome":nome,"notas":notas,"media":media,
        "situacao":situacao
    })
    return alunos
#5°função exibir
def exibir(alunos):
    if alunos:
        for i in alunos: 
            print(f"""
    Nome: {alunos['nome']},
    Notas: {alunos['notas']},
    média: {alunos['media']},
    situação: {alunos['situacao']}""")

    

#6°função editar
#7°função alunos aprovados e reprovados
#8°menu interativo
#MVC=modelo-visão-controlador
#M=model-lógica da aplicação
def main():
    alunos=[]
    while True:
        print("""
            (1) Cadastrar alunos
            (2) exibir alunos""")
#V=view-interface de usuário

#C=controller-intermediário entre o model e view
        escolha = input("")
        if escolha == "1":
            alunos.append(cadastro_alunos())
        elif escolha == "2":
            exibir(alunos)

main()