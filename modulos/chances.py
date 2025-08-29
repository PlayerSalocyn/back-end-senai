def calcular_chance(anomalia, trabalho, funcionario):
    """
    Calcula chance de sucesso baseado no método da anomalia e atributo correto do funcionário.
    """
    # Mapeamento trabalho -> atributo
    atributos = {
        "Toque": "Instinto",
        "Observação": "Competência",
        "Confiança": "Disciplina",
        "Compreensão": "Filosofia"
    }

    # Descobre qual atributo usar
    atributo = atributos[trabalho]
    nivel = funcionario[atributo]  

    # Mantém o nível no máximo 5 (pois a tabela da anomalia vai de 1 a 5)
    nivel = min(nivel, 5)

    # Pega a dificuldade correspondente
    dificuldade = anomalia["Métodos"][trabalho][nivel]

    # Conversão palavra -> probabilidade
    mapa_chances = {
        "muito baixo": 0.2,
        "baixo": 0.35,
        "médio": 0.55,
        "alto": 0.75,
        "muito alto": 0.9
    }

    return mapa_chances[dificuldade]