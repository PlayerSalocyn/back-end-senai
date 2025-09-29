#1° função validar o nome do aluno
def validar_nome():
    while True:
        nome= input("Digite ")
#2° função validar as notas
    notas=[]
    for i in range(1,3):
        nota=float(input(
            f"Digite a nota:{i}"
        ))
        if nota <= 0 or nota <=10:
            notas.append(nota)
            break
        else:
            print("Nota inválida")
    return notas
#3° função média
def media(notas):
    media = sum(notas)/len(notas)
    situacao = "aprovado" if media >= else "reprovado"
    return media,situacao
#4° função cadastro
def cadastro_alunos(alunos):
    alunos = []
    nome= validar_nome()
    notas = validar_notas()
    media, situacao= calcular_media(notas)
    alunos.append({
        "nome":nome, "notas": notas, "media":media, "situacao": situacao
    })

#5° função exibir
#6° função editar
#7° função aluno aprovados e reprovados
#8° menu interativo
#MVC=modelo-visão-controlador
#M=model - lógica da aplicação
#V=view - interface de usuário
#C=controller-intermediário entre o model e view