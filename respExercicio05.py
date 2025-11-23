class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        print("=== Dados do Funcionário ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"salário: {self.salario}")

if __name__ == "__main__":
    funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
    funcionario.exibir_dados()
