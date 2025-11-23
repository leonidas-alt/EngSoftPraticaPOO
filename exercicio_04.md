7# Exercício 04 - Herança Simples (Especialização)

## Objetivo
Usar Herança para criar classes especializadas.

## Descrição do Exercício
Implemente herança criando uma hierarquia de classes.

### Requisitos:

1. Crie uma classe base chamada **Pessoa** com atributos:
   - nome
   - cpf
   - data_nascimento

2. Adicione um método `apresentar()` na classe Pessoa que retorna uma apresentação básica.

3. Crie duas classes filhas que herdam de Pessoa:
   - **Funcionario**: deve adicionar o atributo `cargo`
   - **Tutor**: deve adicionar o atributo `area_atuacao`

4. A classe **Tutor** deve sobrescrever o método `apresentar()` para incluir sua área de atuação.

## Entrega
Crie um arquivo chamado `respExercicio04.py` com a implementação das classes com herança.

## Exemplo de Uso
```python
funcionario = Funcionario("João Silva", "123.456.789-00", "01/01/1990", "Secretário")
tutor = Tutor("Maria Santos", "987.654.321-00", "15/05/1985", "Programação")

print(funcionario.apresentar())
print(tutor.apresentar())
```

## Exemplo de Saída Esperada
```
Olá, sou João Silva, CPF: 123.456.789-00
Olá, sou Maria Santos, CPF: 987.654.321-00, atuo na área de Programação
```