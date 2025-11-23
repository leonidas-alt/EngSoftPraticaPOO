class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []
    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")
    
    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")
    
    def adicionar_professor(self, professor):
        self.professores.append(professor)
    
    def listar_professores(self):
        print(f"Professores do Departamento {self.nome} ({self.sigla}):")
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            for p in self.professores:
                print(f"- {p}")

if __name__ == "__main__":
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")

    dept_exatas.adicionar_professor("Carlos Almeida")
    dept_exatas.adicionar_professor("Mariana Dias")

    dept_humanas.adicionar_professor("Fernanda Silva")

    dept_exatas.listar_professores()
    dept_humanas.listar_professores()