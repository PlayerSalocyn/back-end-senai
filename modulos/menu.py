def menu(opcoes, colunas, numerar=True):
    import shutil
    import textwrap
    from modulos.cores import cores
    largura = (shutil.get_terminal_size().columns) - 1
    largura_colunas = largura // colunas

    opcoes_quebradas=[]


    for i, opcao in enumerate(opcoes, start=1):
        prefixo = ""
        if numerar:
            prefixo = f"[{i}]"
        texto = prefixo + opcao
        linha = textwrap.wrap(texto, width=largura_colunas-1) or [texto]
        opcoes_quebradas.append(linha)
    # Descobre quantas linhas no máximo existem em cada "linha de colunas"
    for bloco in range(0, len(opcoes_quebradas), colunas):
        grupo = opcoes_quebradas[bloco:bloco+colunas]
        max_linhas = max(len(item) for item in grupo)

        # imprime linha por linha dentro do grupo
        for l in range(max_linhas):
            for item in grupo:
                linha = item[l] if l < len(item) else ""
                print(linha.ljust(largura_colunas), end="")
            print()  # quebra depois de cada linha do grupo