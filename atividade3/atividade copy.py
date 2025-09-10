import sqlite3

ALUNOS_DB = "alunos.db"

conexao_A = sqlite3.connect(ALUNOS_DB)
cursor_A = conexao_A.cursor()
cursor_A.execute('''CREATE TABLE IF NOT EXISTS alunos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome  VARCHAR (100) NOT NULL,
               data_nasc DATE NOT NULL,
               matricula INT NOT NULL)

''')

conexao_A.commit()


CURSOS_DB = "cursos.db"

conexao_C = sqlite3.connect(CURSOS_DB)
cursor_C = conexao_C.cursor()
cursor_C.execute('''CREATE TABLE IF NOT EXISTS cursos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR (100) NOT NULL,
               periodo VARCHAR (20) NOT NULL)

''')

conexao_C.commit()


PROFESSORES_DB = "professores.db"

conexao_P = sqlite3.connect(PROFESSORES_DB)
cursor_P = conexao_P.cursor()
cursor_P.execute('''CREATE TABLE IF NOT EXISTS professores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome  VARCHAR (100) NOT NULL,
               disciplina VARCHAR (100) NOT NULL,
               matricula INT NOT NULL)

''')

conexao_P.commit()





class Curso:
    def __init__(self,nome,periodo):
        self.nome= nome
        self.periodo=periodo
        cursor_C.execute('''INSERT INTO cursos (nome,periodo) VALUES (?,?)''',
                         (self.nome, self.periodo))
        conexao_C.commit()
    def __str__(self):
        return f"Curso: {self.nome} - Período: {self.periodo}."

#Class pai para alunos e professores
class Pessoa:
    def __init__(self,nome,data_nasc,matricula):
        self.nome=nome
        self.data = data_nasc
        self.matricula = matricula
#classe filhos professor e aluno
class Professor(Pessoa):
    def __init__(self, nome, disciplina, matricula):
        super().__init__(nome, None, matricula)
        self.disciplina = disciplina
        cursor_P.execute('''INSERT INTO professores (nome,disciplina,matricula) VALUES (?,?,?)''',
                         (nome, self.disciplina, matricula))
        conexao_P.commit()
    def __str__(self):
        return f"""Professor(a): {self.nome}
Disciplina: {self.disciplina} -
Matrícula: {self.matricula}
"""
class Aluno(Pessoa):
    def __init__(self, nome, data_nasc, matricula):
        super().__init__(nome, data_nasc, matricula)
        cursor_A.execute('''INSERT INTO alunos (nome,data_nasc,matricula) VALUES (?,?,?)''',
                         (self.nome, self.data, self.matricula))
        conexao_A.commit()
    def __str__(self):
        return f"""
        Aluno(a): {self.nome}
        Matrícula: {self.matricula}
        Documento: {self.data}
"""

#class principal
class SistemaEscolar:
    def __init__(self):
        #lista para alunos, professores e cursos
        self.alunos = []
        self.professores = []
        self.cursos = []
    #métodos do sistema, listar, incluir
    #pesquisar
    #método aluno
    def listar_alunos(self):
        cursor_A.execute("SELECT * FROM alunos")
        alunos = cursor_A.fetchall()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in alunos:
                
                print(f"Nome: {aluno[1]}")
                print(f"Data_nasc: {aluno[2]}")
                print(f"Matrícula: {aluno[3]}")
                print("-" * 30)


    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        documento = input("Digite o documento do alunos: ")
        aluno = Aluno(nome, documento, matricula)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado!")
    def excluir_aluno(self):
        self.listar_alunos()
        if self.alunos:
            indice = int(input("Digite o índice a ser excluído"))
            if 0 < indice < len(self.alunos):
                aluno_excluido = self.alunos.pop(indice)
                print(f"Aluno {aluno_excluido} foi excluído")
            else:
                print("Índice inválido")
    def pesquisar_aluno(self):
        termo = input("Nome do aluno para pesquisar.").lower()
        encontrados = [
            a for a in self.alunos if termo in a.nome.lower()
        ]
        if encontrados:
            for i in encontrados:
                print(i)
        else:
            print("Aluno não encontrado.")

    def listar_professores(self):
        cursor_P.execute("SELECT * FROM professores")
        professores = cursor_P.fetchall()
        if not professores:
            print("Nenhum professor cadastrado.")
            return
        for prof in professores:
                
                print(f"Nome: {prof[1]}")
                print(f"Disciplina: {prof[2]}")
                print(f"Matrícula: {prof[3]}")
                print("-" * 30)
    
    def incluir_professor(self):
        nome = input("Digite o nome do professor: ")
        disciplina = input("Digite a disciplina: ")
        matricula = input("Digite a matrícula: ")
        professor = Professor(nome, disciplina, matricula)
        self.professores.append(professor)
        print(f"Professor {nome} incluído com sucesso!")
    def excluir_professor(self):
        self.listar_professores()
        if self.professores:
            indice = int(input("Digite o índice do professor a ser excluído: "))
            if 0 <= indice < len(self.professores):
                prof_excluido = self.professores.pop(indice)
                print(f"Professor {prof_excluido.nome} excluído.")
            else:
                print("Índice inválido")
    
    def pesquisar_professor(self):
        termo = input("Digite o nome do professor para a pesquisa: ").upper()
        encontrados = [p for p in self.professores if termo in p.nome.upper()]
        if encontrados:
            for prof in encontrados:
                print(prof)
        else:
            print("Professor não encontrado")
    
    def listar_curso(self):
        cursor_C.execute("SELECT * FROM cursos")
        cursos = cursor_C.fetchall()
        if not cursos:
            print("Nenhum curso cadastrado.")
            return
        for curso in cursos:
                
                print(f"Nome: {curso[1]}")
                print(f"Data_nasc: {curso[2]}")
                print("-" * 30)
    
    def incluir_curso(self):
        nome = input("Digite o nome do curso: ")
        periodo = input("Digite o período do curso: ")
        curso = Curso(nome, periodo)
        self.cursos.append(curso)
        print(f"Curso {nome} incluído com sucesso!")

    def excluir_curso(self):
        self.listar_curso()
        if self.cursos:
            indice = int(input("Digite o índice do curso a ser excluído: "))
            if 0 <= indice < len(self.cursos):
                curso_excluido = self.cursos.pop(indice)
                print(f"Curso {curso_excluido.nome} excluído.")
            else:
                print("Índice inválido.")
    
    def pesquisar_curso(self):
        termo = input("Digite o nome do curso para pesquisa: ").upper()
        encontrados = [c for c in self.cursos if termo in c.nome.upper()]
        if encontrados:
            for curso in encontrados:
                print(curso)
            else:
                print("Curso não encontrado.")
    
    def executar(self):
        print("Bem-vindo ao Sistema Escolar!")
        while True:
            print("""
                  0 - sair
                  1 - Ver lista de alunos
                  2 - Incluir novo aluno
                  3 - Excluir aluno
                  4 - Pesquisar aluno
                  5 - Ver lista de professores
                  6 - Incluir novo professor
                  7 - Excluir professor
                  8 - Pesquisar professor
                  9 - Ver lista de curso
                  10 - Incluir novo curso
                  11 - Excluir curso
                  12 - Pesquisar curso
""")
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Saindo do sistema...")
                conexao_A.close()
                conexao_C.close()
                conexao_P.close()
                break
            elif opcao == "1": self.listar_alunos()
            elif opcao == "2": self.incluir_aluno()
            elif opcao == "3": self.excluir_aluno()
            elif opcao == "4": self.pesquisar_aluno()
            elif opcao == "5": self.listar_professores()
            elif opcao == "6": self.incluir_professor()
            elif opcao == "7": self.excluir_professor()
            elif opcao == "8": self.pesquisar_professor()
            elif opcao == "9": self.listar_curso()
            elif opcao == "10": self.incluir_curso()
            elif opcao == "11": self.excluir_curso()
            elif opcao == "12": self.pesquisar_curso()
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.executar()