# Exercício 12 - Princípio Aberto/Fechado (OCP)

## Objetivo
Aplicar o segundo princípio SOLID - Open/Closed Principle (OCP).

## Descrição do Exercício
Implemente um sistema de cálculo de descontos que seja aberto para extensão mas fechado para modificação.

### Requisitos:

1. **Crie uma classe abstrata** `CalculadorDesconto` com método abstrato `calcular(valor)`.

2. **Implemente diferentes tipos de desconto**:
   - **DescontoEstudante**: 10% de desconto
   - **DescontoFuncionario**: 15% de desconto
   - **DescontoVIP**: 20% de desconto

3. **Crie a classe** `ProcessadorPagamento` que aceita qualquer calculadora de desconto.

4. **Demonstre** como adicionar um novo tipo de desconto sem modificar código existente.

## Entrega
Crie um arquivo chamado `respExercicio12.py` com a implementação seguindo o OCP.

## Exemplo de Uso
```python
from abc import ABC, abstractmethod

# Uso do sistema
pagamento = ProcessadorPagamento()
valor_original = 1000.0

# Diferentes tipos de desconto
desconto_estudante = DescontoEstudante()
desconto_funcionario = DescontoFuncionario()

valor_final1 = pagamento.processar(valor_original, desconto_estudante)
valor_final2 = pagamento.processar(valor_original, desconto_funcionario)

print(f"Estudante: R$ {valor_final1}")
print(f"Funcionário: R$ {valor_final2}")
```

## Exemplo de Saída Esperada
```
Estudante: R$ 900.0
Funcionário: R$ 850.0
```