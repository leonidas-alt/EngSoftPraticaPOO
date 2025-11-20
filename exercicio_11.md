# Exercício 11 - Princípio da Responsabilidade Única (SRP)

## Objetivo
Aplicar o primeiro princípio SOLID - Single Responsibility Principle (SRP).

## Descrição do Exercício
Refatore uma classe que viola o SRP, separando suas responsabilidades em classes distintas.

### Código Problemático:
```python
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_salario_liquido(self, descontos):
        return self.salario - descontos
    
    def gerar_relatorio(self):
        return f"Relatório: {self.nome} - {self.cargo} - R$ {self.salario}"
    
    def salvar_no_banco(self):
        print(f"Salvando {self.nome} no banco de dados...")
```

### Requisitos:

1. **Identifique as responsabilidades** da classe Funcionario (dados, cálculos, relatórios, persistência).

2. **Crie classes separadas** para cada responsabilidade:
   - **Funcionario**: apenas dados do funcionário
   - **CalculadoraSalario**: cálculos relacionados a salário
   - **GeradorRelatorio**: geração de relatórios
   - **RepositorioFuncionario**: persistência de dados

3. **Implemente as classes** seguindo o SRP.

4. **Demonstre o uso** das classes refatoradas.

## Entrega
Crie um arquivo chamado `respExercicio11.py` com a implementação refatorada seguindo o SRP.

## Exemplo de Uso
```python
funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
calculadora = CalculadoraSalario()
gerador = GeradorRelatorio()
repositorio = RepositorioFuncionario()

salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
relatorio = gerador.gerar_relatorio(funcionario)
repositorio.salvar(funcionario)
```