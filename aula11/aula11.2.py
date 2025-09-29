class Curso:
    def __init__(self,nome,periodo):
        self.nome= nome
        self.periodo=periodo
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
        super().__init__(nome, disciplina, matricula)
        self.disciplina = disciplina
    def __str__(self):
        return f"""Professor(a): {self.nome}
Disciplina: {self.disciplina} -
Matrícula: {self.matricula}
"""
class Aluno(Pessoa):
    def __init__(self, nome, documento, matricula):
        super().__init__(nome, None, matricula)
        self.documento=documento
    def __str__(self):
        return f"""
        Aluno(a): {self.nome}
        Matrícula: {self.matricula}
        Documento: {self.documento}
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
        if not self.alunos:
            print("nenhum aluno cadastrado.")
        for i, aluno in enumerate(self.alunos):
            print(f"{i} - {aluno}")
    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        documento = input("Digite o documento do alunos: ")
        aluno = Aluno(nome, documento, matricula)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado!")
    def executar_aluno(self):
        self.listar_alunos()
        if self.alunos:
            indice = int(input("Digite o índice a ser excluído"))
            if 0 < indice < len(self.alunos):
                aluno_excluido = self.alunos.pop(indice)
                print(f"Aluno excluído")
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

sistema = SistemaEscolar()
sistema.incluir_aluno()
sistema.listar_alunos()
sistema.pesquisar_aluno()
sistema.executar_aluno()
sistema.incluir_aluno()