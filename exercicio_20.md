# Exercício 20 - Padrão Strategy (Comportamental)

## Objetivo
Implementar o padrão de projeto Strategy para alternar algoritmos dinamicamente.

## Descrição do Exercício
Crie um sistema de cálculo de frete que pode usar diferentes estratégias de cálculo.

### Requisitos:

1. **Interface** `EstrategiaFrete` com método `calcular_frete(peso, distancia)`.

2. **Estratégias concretas**:
   - **FreteNormal**: R$ 5.00 + (peso * 2.0) + (distancia * 0.1)
   - **FreteExpresso**: R$ 15.00 + (peso * 3.0) + (distancia * 0.2)
   - **FreteEconomico**: R$ 2.00 + (peso * 1.0) + (distancia * 0.05)

3. **Classe** `CalculadoraFrete` que:
   - Aceita uma estratégia no construtor
   - Permite trocar estratégia em tempo de execução
   - Método `calcular(peso, distancia)` que usa a estratégia atual

4. **Demonstre** como trocar estratégias dinamicamente.

## Entrega
Crie um arquivo chamado `respExercicio20.py` com a implementação do padrão Strategy.

## Exemplo de Uso
```python
peso = 10.0  # kg
distancia = 100.0  # km

calculadora = CalculadoraFrete(FreteNormal())
print(f"Frete Normal: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteExpresso())
print(f"Frete Expresso: R$ {calculadora.calcular(peso, distancia)}")

calculadora.definir_estrategia(FreteEconomico())
print(f"Frete Econômico: R$ {calculadora.calcular(peso, distancia)}")
```

## Exemplo de Saída Esperada
```
Frete Normal: R$ 35.0
Frete Expresso: R$ 65.0
Frete Econômico: R$ 17.0
```