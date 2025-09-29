#aula 11 POO python
'''
Sistema Escolar com POO em Python construção de um sistema
com alunos professores e cursos.
Menu do sistema.
0 - Sair
1 - Ver lista de alunos
2 - Incluir novo aluno
3 - Excluir aluno
4 - Pesquisar aluno
5 - Ver lista de professores
6 - Incluir novo professor
7 - Excluir professor
8 - Pesquisar professor
9 - Ver lista de cursos
10 - Incluir novo curso
11 - Excluir curso
12 - Pesquisar curso
'''

import mysql.connector

CONFIG_BANCO = {
    'host': 'local',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'alunos'
}
conexao = mysql.connector.connect(**CONFIG_BANCO) #passar chave e valor pra função
#kward python
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS teste2 (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nome VARCHAR(100) NOT NULL,
               saldo FLOAT NOT NULL)''')
conexao.commit()
nome = input("Nome: ")
saldo = float(input("digite o seu saldo R$:"))
cursor.execute('''INSERT INTO teste (nome,saldo) VALUES (
               %s, %s)''', (nome, saldo))
conexao.commit()
conexao.close()

