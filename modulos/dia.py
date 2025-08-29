
def dia(num, anomalias, funcionarios):
    from modulos.som import sons
    from modulos.mensagem import msg
    from modulos.menu import menu
    from modulos.limpar import limpar_terminal
    from modulos.ost import OST
    from modulos.tarefa import tarefa
    from modulos.problemas import calc_problemas
    import time
    em_andamento = True
    corredores = ["Corredores do Oeste", "Corredores do Sul", "Corredores do Leste"]
    opções = corredores + []
    limpar_terminal()
    for i in anomalias:
        opções.append(i["Nome"])
    Meta = num * 10
    pontos_de_pesquisa = 0
    Problemas = 0
    while em_andamento:
        status = [
            f"Pontos de pesquisa: {pontos_de_pesquisa}/{Meta}",
            f"Nível de perigo: {Problemas}"
        ]
        if pontos_de_pesquisa >= Meta:
            em_andamento = False
            break
        msg(f"Dia {num}", "AZ")
        print("\n\n\n")
        menu(status, 2, False)
        menu(opções, 3)
        ação = input("\n\nPróxima ação:")
        limpar_terminal()
        if ação.isdigit() and 1 <= int(ação) <= len(opções):
            indice = int(ação) - 1
            escolha = opções[indice]
            if escolha in corredores:
                msg("Não há nada lá", "P")
                time.sleep(3)
            else:
                anomalia = next(a for a in anomalias if a["Nome"] == escolha)
                funcionario, resultado, novos_pontos = tarefa(funcionarios, anomalia)
                limpar_terminal()
                if resultado == "Morto":
                    msg(f"O funcionário {funcionario} Morreu em seu local de trabalho", "AM")
                    Problemas = calc_problemas(1, Problemas)
                    
                elif resultado == "Insano":
                    msg(f"O funcionário {funcionario} Enloqueceu em seu local de trabalho", "AM")
                    Problemas = calc_problemas(1, Problemas)

                elif resultado == "Sucesso":
                    msg(f"O funcionário {funcionario} fez um ótimo trablho e arrecadou {novos_pontos} pontos de pesquisa!", "AZ")
                pontos_de_pesquisa += novos_pontos
                
                
                    

                
        else:
            msg("Escolha o número que representa sua ação! ","P")



