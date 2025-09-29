"""
Nome: Nycolas Marques
RA: 24271524
Data: 18/08
"""


def conectar_bd():
    import sqlite3

    Banco = "alunos.db"
    conexao = sqlite3.connect(Banco)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota REAL NOT NULL,
            media REAL NOT NULL,
            situacao INTEGER NOT NULL)''')
    conexao.commit()
    return conexao, cursor