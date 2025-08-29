def gerar_nome():
    import requests

    resp = requests.get('https://randomuser.me/api/?nat=eua&results=5')
    dados = resp.json()
    for user in dados['results']:
        nome = user['name']['first'] + ' ' + user['name']['last']
    return nome



def criar_funcionario(nome=None, instinto=None, competencia=None, disciplina=None, filosofia=None):
    import random
    
    if nome is None:
        nome = gerar_nome()

    instinto = instinto if instinto is not None else random.randint(1, 5)
    competencia = competencia if competencia is not None else random.randint(1, 5)
    disciplina = disciplina if disciplina is not None else random.randint(1, 5)
    filosofia = filosofia if filosofia is not None else random.randint(1, 5)

    vida = 10 + disciplina + instinto * 7
    sanidade = 10 + filosofia + competencia * 6
    max_vida = vida
    max_sanidade = sanidade

    return {
        "Nome": nome,
        "Instinto": instinto,
        "Competência": competencia,
        "Disciplina": disciplina,
        "Filosofia": filosofia,
        "Vida": vida,
        "MAX_Vida": max_vida,
        "Sanidade": sanidade,
        "MAX_Sanidade": max_sanidade,
        "XP": {  # XP separado por atributo
            "Instinto": 0,
            "Competência": 0,
            "Disciplina": 0,
            "Filosofia": 0
        },
        "Status": "Disponível"
    }

# a = gerar_funcionário()
# print(a)
def aplicar_dano(funcionario, anomalia):
    import random

    dano_min, dano_max = anomalia["Dano"]
    dano = random.randint(dano_min, dano_max)

    tipo = anomalia["Tipo de Dano"]

    if tipo == "físico":
        funcionario["Vida"] -= dano
    elif tipo == "mental":
        funcionario["Sanidade"] -= dano
    elif tipo == "existencial":
        funcionario["Vida"] -= dano
        funcionario["Sanidade"] -= dano

    # Verifica se morreu ou enlouqueceu
    if funcionario["Vida"] <= 0:
        funcionario["Status"] = "Morto"
    elif funcionario["Sanidade"] <= 0:
        funcionario["Status"] = "Insano"

def nivel_do_atributo(trabalho):


    Nível = {
        "Toque": "Instinto",
        "Observação": "Competência",
        "Confiança": "Disciplina",
        "Compreensão": "Filosofia"
    }
    return Nível[trabalho]

def ganhar_xp(funcionario, trabalho, xp_ganho=1):
    # Mapeia trabalho -> atributo
    atributos = {
        "Toque": "Instinto",
        "Observação": "Competência",
        "Confiança": "Disciplina",
        "Compreensão": "Filosofia"
    }
    
    atributo = atributos[trabalho]
    funcionario["XP"][atributo] += xp_ganho

    # Sistema de level up: cada 10 XP sobe 1 ponto no atributo
    xp_atual = funcionario["XP"][atributo]
    if xp_atual >= (10*funcionario[atributo]):
        funcionario["XP"][atributo] = xp_atual - 10*funcionario[atributo]  # mantém excesso
        funcionario[atributo] += 1  # sobe nível
        return f"{funcionario['Nome']} subiu para {atributo} {funcionario[atributo]}!"
    
    return None
