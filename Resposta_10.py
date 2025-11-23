class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
    
    def apresentar(self):
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):
    def __init__(self, nome, idade, cpf, curso):
        super().__init__(nome, idade, cpf)
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, departamento, salario):
        super().__init__(nome, idade, cpf)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

# Testando o código
estudante = Estudante("João", 20, "123.456.789-00", "Engenharia")
professor = Professor("Dr. Silva", 45, "987.654.321-00", "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
estudante.adicionar_nota(8.5)
estudante.adicionar_nota(9.0)
print(f"Média do estudante: {estudante.calcular_media()}")