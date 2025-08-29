
def seleção(dia_):

    import random
    from modulos.mensagem import msg
    from modulos.menu import menu
    from modulos.limpar import limpar_terminal
    from modulos.anomalias import anomalias
    from modulos.cores import cores

    resetar = cores["resetar"]
    cor = cores["P"]
    if dia_ < 2: 
        filtradas = [a for a in anomalias if a["Classe"] in ["E"]]
        candidatas = random.sample(filtradas, 3)
    elif dia_ < 4:
        filtradas = [a for a in anomalias if a["Classe"] in ["E", "D"]]
        candidatas = random.sample(filtradas, 3)

    estrutura = [f"{cor} {i['Sinopse']}" for i in candidatas]

    msg("Qual vai ser a anomalia de hoje?", "P")
    while True:
        menu(estrutura, 3)
        resposta = input("\n")
        limpar_terminal()
        if resposta.isdigit() and 1 <= int(resposta) <= 3:
            indice = int(resposta) - 1
            escolhida = candidatas[indice]
            break
        else:
            msg("Escolha o número da anomalia que vamos estudar", "P")
    return escolhida


# a = seleção()
# print(a)