class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
        return f"Olá, sou {self.nome}, CPF: {self.cpf} e Data de Nascimento: {self.data_nascimento}"

class Funcionario(Pessoa):
     def __init__(self, nome, cpf, data_nascimento, cargo):
         super().__init__(nome, cpf, data_nascimento)
         self.cargo = cargo

class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
         super().__init__(nome, cpf, data_nascimento)
         self.area_atuacao = area_atuacao
    def apresentar(self):
        return f"Olá, sou {self.nome}, CPF: {self.cpf}, atuo na área de {self.area_atuacao}"

if __name__ == "__main__":
    funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
    tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

    print(funcionario.apresentar())
    print(tutor.apresentar())    