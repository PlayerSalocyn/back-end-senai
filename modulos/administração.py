def administrar(PP, funcionários, anomalias, _dia):
    from modulos.menu import menu
    from modulos.mensagem import msg
    from modulos.limpar import limpar_terminal
    from modulos.melhorar_funcionário import melhorar_funcionario
    opções_A = []
    opções_F = []
    for i in anomalias:
        opções_A.append(i["Nome"])
    for i in funcionários:
        opções_F.append(f"{i["Nome"]}")
    opções_A.append("Voltar")
    opções_F.append("Voltar")
        
    while True:
        limpar_terminal()
        msg(f"Dia: {_dia}", "AZ")
        opções = [
            "Anomalias",
            "funcionários",
            "Começar o dia"
        ]
        menu(opções, 2)
        escolha = input("\n")
        limpar_terminal()
        if escolha == "1":
            continue
        elif escolha == "2":
            while True:
                msg("Funcionários", "AZ")
                menu(opções_F, 3)

                try:
                    idx = int(input("\n")) - 1
                    if 0 <= idx < len(opções_F):
                        if "Voltar" == opções_F[idx]:
                            break
                        f = funcionários[idx]
                        limpar_terminal()
                        opções_FD = [
                            f"Vida: {f['MAX_Vida']}",
                            f"Sanidade: {f['MAX_Sanidade']}",
                            f"Instinto: {f['Instinto']}",
                            f"Competência: {f['Competência']}",
                            f"Disciplina: {f['Disciplina']}",
                            f"Filosofia: {f['Filosofia']}"
                        ]
                        msg(f"Dados de {f['Nome']}", "AZ")
                        menu(opções_FD, 2, False)
                        print("\n\n\n")
                        opções_FD2 = [
                            "melhorar funcionário",
                            "voltar"
                        ]
                        menu(opções_FD2, 2)
                        while True:
                            escolha = input("\n")
                            if escolha == "1":
                                limpar_terminal()
                                PP = melhorar_funcionario(f, PP)
                                break
                            elif escolha == "2":
                                break
                            else:
                                continue

                        
                except ValueError:
                    pass
        