def melhorar_funcionario(funcionario, PP):
    from modulos.menu import menu
    from modulos.mensagem import msg
    from modulos.limpar import limpar_terminal

    # Função para calcular custo de upgrade
    def calcular_custo(valor):
        if valor >= 5:  # limite
            return "Max"
        elif valor == 1:
            return 5
        else:
            return 5 * (3 ** (valor - 1))

    atributos = ["Instinto", "Competência", "Disciplina", "Filosofia"]

    while True:
        limpar_terminal()
        msg(f"{funcionario['Nome']}", "AZ")
        print(f"Pontos de Pesquisa: {PP}\n")

        # Monta menu dinamicamente com custo
        opções = []
        for atributo in atributos:
            valor = funcionario[atributo]
            custo = calcular_custo(valor)
            opções.append(f"{atributo}: {valor}  (Custo: {custo})")
        opções.append("Voltar")

        menu(opções, 1)

        escolha = input("\nSelecione um atributo para melhorar: ")

        if escolha.isdigit():
            escolha = int(escolha)
        else:
            continue

        if escolha == len(opções):  # "Voltar"
            break
        elif 1 <= escolha <= len(atributos):
            atributo = atributos[escolha - 1]
            valor = funcionario[atributo]
            custo = calcular_custo(valor)

            if custo == "Max":
                print(f"\n{atributo} já está no nível máximo!")
                input("\nPressione ENTER para continuar")
                continue

            if PP >= custo:
                funcionario[atributo] += 1
                PP -= custo
                print(f"\n{atributo} de {funcionario['Nome']} melhorado para {funcionario[atributo]}!")
                print(f"PP restantes: {PP}")
                input("\nPressione ENTER para continuar")
            else:
                print("\nPontos de Pesquisa insuficientes!")
                input("\nPressione ENTER para continuar")
        else:
            continue

    return PP