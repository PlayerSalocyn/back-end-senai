"""
Nome: Nycolas Marques
RA: 24271524
Data: 18/08
"""


from dados import conectar_bd

class Aluno:
    def __init__(self, nome):
        self.nome=nome
        self.notas=[]
        self.media=0.0
        self.situacao=""
    def adicionar_notas(self):
        for i in range(1,4):
            while True:
                try:
                    nota= float(input(
                        f"Digite a nota {i} entre 0 e 10. "))
                    if nota >= 0:
                        if nota <= 10:
                            self.notas.append(nota)
                            break
                    else: print("ERRO nota entre 0 a 10")
                except ValueError: print(
                    "Erro digite uma nota válida!"
                )
    #método para média e situação
    def calcular_media(self):
        self.media=sum(self.notas)/len(self.notas)
        self.situacao="Aprovado" if self.media >= 6 else "Reprovado"
    #método para exibir resultados
    def exibir_dados(self):
        conexao, cursor = conectar_bd()
        print(f"""
            Nome: {self.nome}
            Notas:{self.notas}
            Média: {self.media:.2f}
            Situação: {self.situacao}""")
        notas = str(self.notas)
        cursor.execute("""
        INSERT INTO alunos (
                nome,nota,media,situacao) VALUES (?,?,?,?)
        """, (self.nome,notas,self.media,self.situacao))
        conexao.commit()