def tarefa(funcionarios, anomalia):
    from modulos.anomalias import anomalias
    from modulos.chances import calcular_chance
    from modulos.mensagem import msg
    from modulos.menu import menu
    from modulos.funcionarios import aplicar_dano, ganhar_xp
    from modulos.limpar import limpar_terminal
    from modulos.exibir_imagem import show_image
    from modulos.cores import cores
    import random
    import time
    loop_tarefa = True
    show_image(anomalia["Imagem"])
    pontos_de_pesquisa = 0
    while loop_tarefa:
        msg(f"Você tem certeza que quer começar o trabalho com: {anomalia['Nome']}?", "P")
        resposta = input("Y/N  ").upper()
        if resposta == "Y":
            if funcionarios:
                resetar = cores["resetar"]
                vm = cores["VM"]
                az = cores["AZ"]

                func_opcoes = [f"{f['Nome']} ({f['Status']}) Vida: {f['Vida']}/{f['MAX_Vida']} Sanidade: {f['Sanidade']}/{f['MAX_Sanidade']}" for f in funcionarios]

                func_opcoes.append("Cancelar")

                menu(func_opcoes, 3)

                escolha_func = input("\nSelecione o funcionário: ")

                if escolha_func.isdigit() and 1 <= int(escolha_func) <= len(func_opcoes):
                    idx_func = int(escolha_func) - 1
                    if idx_func == len(func_opcoes) - 1:  # Cancelar
                        return None, None, 0

                    funcionario = funcionarios[idx_func]

                    # Escolher o tipo de trabalho
                    trabalhos = ["Toque", "Observação", "Confiança", "Compreensão"]
                    msg("Qual trabalho será?", "P")
                    menu(trabalhos, 2)
                    resposta = input("\nEscolha: ")
                    limpar_terminal()
                    

                    if resposta.isdigit() and 1 <= int(resposta) <= len(trabalhos):
                        tipo_trab = trabalhos[int(resposta) - 1]

                        msg(f"{funcionario['Nome']} começou a realizar {tipo_trab} em {anomalia['Nome']}...", "AZ")
                        time.sleep(2)

                        # Para cada ponto de pesquisa, roda um "tick"
                        for i in range(anomalia["pesquisa"]):
                            if funcionario["Status"] != "Disponível":
                                break  # funcionário já morreu/ficou louco

                            # chance com base no módulo pronto
                            chance = calcular_chance(anomalia, tipo_trab, funcionario)
                            rolagem = random.randint(1, 100)
                            sucesso = rolagem <= (chance * 100)

                            if sucesso:
                                msg(f"({i+1}/{anomalia['pesquisa']}) ✅ {funcionario['Nome']} obteve sucesso.", "AZ")
                                resultado = ganhar_xp(funcionario, tipo_trab)
                                if resultado:
                                    msg(resultado, "AZ")
                                pontos_de_pesquisa += 1
                            else:
                                msg(f"({i+1}/{anomalia['pesquisa']}) ❌ {funcionario['Nome']} falhou.", "P")
                                aplicar_dano(funcionario, anomalia)
                                if funcionario["Vida"] <= 0:
                                    funcionario["Status"] = "Morto"
                                    return funcionario["Nome"], "Morto", pontos_de_pesquisa
                                elif funcionario["Sanidade"] <= 0:
                                    funcionario["Status"] = "Insano"
                                    return funcionario["Nome"], "Insano", pontos_de_pesquisa
                                    

                            time.sleep(1)
                        return funcionario["Nome"], "Sucesso", pontos_de_pesquisa
                            

                            

        elif resposta == "N":
            return None, None, 0
        else:
            msg("Y (YES), N (NÃO)", "P")