class Professor:
    def __init__(self, nome, departamento, salario):
        self.nome=nome
        self.departamento=departamento
        self.__salario=salario

    def get_salario(self):
        return self.__salario
    def set_salario(self, novo_salario):
        if novo_salario >= 0:
            self.__salario=novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo!")
  
prof = Professor("Dr. Silva", "Computação", 5000.0)
print(f"Salário atual: R$ {prof.salario}")
prof.salario = 6000.0  # Deve funcionar
print(f"Novo salário: R$ {prof.salario}")
prof.salario = -1000.0  # Deve dar erro
print(f"Salário após tentativa inválida: R$ {prof.salario}")
