def centralizar_multilinha(texto, largura):
    import textwrap
    # quebra o texto em várias linhas que cabem no terminal
    linhas = textwrap.wrap(texto, largura)
    # centraliza cada linha separadamente
    return [linha.center(largura) for linha in linhas]


def msg(texto, tipo):
    import random
    from colorama import init, Fore, Back, Style
    from modulos.som import sons
    import shutil
    from modulos.cores import cores
    largura = (shutil.get_terminal_size().columns) -1


    resetar = cores["resetar"]

    cor = cores.get(tipo, Fore.WHITE)

    linhas = centralizar_multilinha(texto, largura)



    if tipo in ["B", "AZ"]:
        valor = random.randint(1,3)
        if valor == 1:
            sons["notificação_1"].play()
        elif valor == 2:
            sons["notificação_2"].play()
        elif valor == 3:
            sons["notificação_3"].play()

    print(cor, "#"*largura, resetar)
    for linha in linhas:
        print(cor, linha, resetar)
    print(cor, "#"*largura, resetar)