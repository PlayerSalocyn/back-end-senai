def eventos(dia_):
    from modulos.mensagem import msg
    from modulos.limpar import limpar_terminal
    from modulos.menu import menu
    import time
    limpar_terminal()
    time.sleep(2)
    if dia_ == 1:
        msg("Muito bem gerente, você concluiu seu primeiro dia com sucesso", "AZ")
        time.sleep(3)
        msg("Mas ainda temos um longo caminho pela frente, esse é só a ponta do iceberg", "AZ")
        time.sleep(3)
        msg('Aquela anomalia que você estudou era "Classe E" sabia? Faz parte do grupo de anomalias mais fáceis de estudar', "AZ")
        time.sleep(4)
        msg("O que você achou dela?", "AZ")
        time.sleep(1)
        opcoes = [
            "Foi bem tranquilo",
            "Eu não achei tão fácil..."
        ]
        menu(opcoes, 2)
        while True:
            escolha = input("\n")
            if escolha == "1":
                msg("É bom saber disso, acho que estamos em boas mãos por enquanto", "AZ")
                time.sleep(3)
                break
            elif escolha == "2":
                msg("Não era essa a resposta que eu esperava", "AZ")
                time.sleep(3)
                msg("Mas você vai se acostumar com seu trabalho, não se preocupe", "AZ")
                time.sleep(3)
                break
            else:
                continue
        msg("Mudando de assunto, eu conversei com os superiores e achamos que seja melhor eu assumir uma forma mais humana", "AZ")
        time.sleep(3)
        opcoes = [
            "Como assim?",
            "Eu concordo",
            "Eu acho que você está boa assim mesmo"
        ]
        menu(opcoes, 2)
        while True:
            escolha = input("\n")
            if escolha == "1":
                msg("Não é bom pra sanidade do meu gerente apenas uma máquina ser a única fonte social dele", "AZ")
                time.sleep(4)
                msg("Claro que eu ainda serei uma IA, mas enquanto eu estiver parecendo com um humano, iso não importará mais", "AZ")
                time.sleep(5)
                break
            elif escolha == "2":
                break
            elif escolha == "3":
                msg("Eu agradeço o elogio, mas essas ordens vão um pouco além do seu cargo", "AZ")
                time.sleep(4)
                break
            else:
                continue
        msg("A construção do meu corpo humano terminará nos próximos dias", "AZ")
        time.sleep(3)
        msg("Te vejo amanhã gerente", "AZ")
        time.sleep(1)
        escolha = input("\nAvançar: ")
    limpar_terminal()

