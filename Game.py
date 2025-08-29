import random
import time
from colorama import init, Fore, Back, Style
import os
import sys
import pygame


from modulos.som import sons
from modulos.mensagem import msg
from modulos.menu import menu
from modulos.limpar import limpar_terminal
from modulos.ost import OST
from modulos.seleção import seleção
from modulos.dia import dia
from modulos.funcionarios import criar_funcionario

init()
pygame.mixer.init()







#início
limpar_terminal()
pygame.mixer.music.load(OST["inicio"])
pygame.mixer.music.play(loops=-1)
msg("Seja Bem vindo!", "AZ")
time.sleep(2)
msg("É sua primeira vez aqui gerente?", "AZ")
time.sleep(2)
while True:
    resposta = input("Y/N: ").upper()
    if resposta == "Y":
        break
    elif resposta == "N":
        continue
    else:
        msg("Responda com Y (YES) ou N (NÃO) por favor", "P")
limpar_terminal()
time.sleep(2)
msg("Muito Bem! É um prazer tê-lo aqui gerente!", "AZ")
time.sleep(2)
msg("Eu sou Ágatha, uma IA criada para te ajudar com sua pesquisa", "AZ")
time.sleep(2)

tutorial = True
while tutorial:
    msg("Você quer que eu te passe as instruções? ou deseja começar logo seu trabalho?", "AZ")
    opcoes = [
        "Ver instruções",
        "Pular"
    ]
    menu(opcoes, 2)
    resposta = input("")
    limpar_terminal()
    if resposta == "1":
        msg("Boa escolha! Você já é bem melhor que o último gerente desse departamento", "AZ")
        time.sleep(2)
        msg("Sua missão aqui é estudar anomalias paranormais que nossa equipe conseguiu capturar", "AZ")
        time.sleep(2)
        msg("Para terminar seu dia, você precisa alcançar uma Meta de pesquisa tirado dessas anomalias, que vai aumentando a cada dia", "AZ")
        time.sleep(3)
        msg("Isso não será possível sem seus funcionários, eles farão o necessário quando estiverem na sala da anomalia", "AZ")
        time.sleep(2)
        msg("Cada Anomalia tem uma preferência de estudo, algumas não gostam de contato físico, outras não gostam de ser encaradas.", "AZ")
        time.sleep(3)
        msg("Infelizmente, nossos estudos não tem capacidade de te fornecer uma bola de cristal, então já está nos planos que alguns funcionários provavelmente vão morrer", "AZ")
        time.sleep(4)
        while True:
            msg("Existe mais alguma dúvida gerente?", "AZ")
            opcoes = [
                "Sobre as anomalias",
                "Classe de anomalias",
                "Sobre os funcionários",
                "Sobre o dia",
                "Sobre a pesquisa",
                "Isso é tudo"
            ]
            menu(opcoes, 2)
            resposta = input("")
            limpar_terminal()
            if resposta == "1":
                msg("Claro! Anomalias são criaturas geralmente perigosas, algumas são simplesmente aberrações, outras são seres paranormais que provavelmente vieram de outro mundo", "AZ")
                time.sleep(4)
                msg("Quanto mais perigosa a anomalia, mais pontos de pesquisa você receberá!", "AZ")
                time.sleep(3)
                msg("É bem difícil compreendê-las, já que elas são bem diferentes de uma pra outra", "AZ")
                time.sleep(2)
                input("OK: ")
                limpar_terminal()
            elif resposta == "2":
                msg("Cada Anomalia possui um nível de perigo maior que a outra, nós categorizamos de E a S", "AZ")
                time.sleep(4)
                msg("Anomalias de Classe E são praticamente inofensivas por causarem pouco dano ou nenhum a quem estiver perto", "AZ")
                time.sleep(3)
                msg("Anomalias de Classe D podem ser perigosas para civis ou pessoas sem treinamento necessário", "AZ")
                time.sleep(3)
                msg("Anomalias de Classe C já podem ser fatais até com aqueles bem treinados, basta errar um movimento que o funcionário nunca mais volta da sala", "AZ")
                time.sleep(5)
                msg("Anomalias de Classe B são temidas até pelos funcionários mais experiêntes, seu poder destrutivo pode massacrar um funcionário mediano em questão de poucos segundos", "AZ")
                time.sleep(5)
                msg("Anomalias de Classe A é um perigo eminente, seus funcionários torcem pra você não envia-los pra elas, seu poder destrutivo é de uma cidade inteira", "AZ")
                time.sleep(5)
                msg("Anomalias de Classe S São exageradamente destrutivas, com risco de destruição global caso elas escampem da contenção! Por favor gerente, pense bem nas suas ações quando for estuda-las...", "AZ")
                input("OK: ")
                limpar_terminal()
            elif resposta == "3":
                msg("Você vai começar com apenas um funcionário iniciante para fazer as tarefas do dia", "AZ")
                time.sleep(3)
                msg("caso seja pouco, você pode contratar mais funcionários no fim do dia", "AZ")
                time.sleep(3)
                msg("Cada funcionário tem sua competência, disciplina, filosofia e instinto que são peças importantes dependendo da anomalia que envia-los", "AZ")
                time.sleep(5)
                msg("Esses atributos aumento conforme o funcionário pratica eles no trabalho. Você pode também contratar funcionário com atributos avançados  para adiantar", "AZ")
                time.sleep(4)
                input("OK: ")
                limpar_terminal()
            elif resposta == "4":
                msg("durante o dia, você vai enviar seus funcionários para as contenções e estudar as anomalias", "AZ")
                time.sleep(3)
                msg("No entanto, Caso o trabalho tenha resultado negativo, a anomalia pode escapar e andar pelo departamento", "AZ")
                time.sleep(4)
                msg("Caso você já tenha conseguido a meta para finalizar o dia, você pode finaliza-lo mesmo com anomalias fugitivas, porém você receberá menos recursos no próximo dia", "AZ")
                time.sleep(5)
                msg("Anomalias diversas podem invadir seu departamento caso o dia esteja demorando, nesse caso, apenas neutralize elas!", "AZ")
                time.sleep(4)
                msg("Algumas contenções podem entrar em colapso de repente, basta enviar um funcionário até lá e tudo vai ficar sob controle", "AZ")
                time.sleep(4)
                msg("Caso o contrário a anomalia vai escapar ou perderemos pontos de pesquisa", "AZ")
                time.sleep(4)
                input("OK: ")
            elif resposta == "5":
                msg("quando o funcionário começar a pesquisa, você vai escolher o método que achar mais eficáz para a anomalia específica", "AZ")
                time.sleep(4)
                msg("trabalho por Toque faz que seu funcionário faz diversas vezes contato físico com a anomalia, aqueles com instinto maior são mais eficientes", "AZ")
                time.sleep(5)
                msg("trabalho por Observação faz que seu funcionário trabalhe de longe apenas observando e criando análises da anomalia, aqueles com maior competência são mais eficientes", "AZ")
                time.sleep(5)
                msg("trabalho por confiança faz que seu funcionário mantenha empatia e afeição pela anormalidade, aqueles com maior disciplina são mais eficientes", "AZ")
                time.sleep(5)
                msg("trabalho por compreensão faz que seu funcionário procure entender e até conversar com a anomalia, aqueles com maior filosofia são mais eficientes", "AZ")
                time.sleep(5)
                msg("Caso você não tenha usado um método eficiente para a anomalidade, ou seu funcionário não ser bom o bastante, existe a possibilidade dele falecer e/ou a anomalia escapar", "AZ")
                time.sleep(5)
                input("OK: ")
            elif resposta == "6":
                tutorial = False
                break
            else:
                msg("Por favor, digite o número de sua escolha", "P")
    elif resposta == "2":
        tutorial = False

limpar_terminal()
msg("Muito bem! Vamos começar o dia...", "AZ")
time.sleep(2)
limpar_terminal()
anomalias = []
funcionários = []

funcionários.append(criar_funcionario(None, 1, 1, 1, 1)) 

for dia_ in range(1, 10):
    pygame.mixer.music.load(OST["Novo_membro"])
    pygame.mixer.music.play(loops=-1)
    nova_anomalia = seleção(dia_)
    pygame.mixer.music.load(OST["Neutro"])
    pygame.mixer.music.play(loops=-1)
    anomalias.append(nova_anomalia)
    dia(dia_, anomalias, funcionários)
    time.sleep(3)