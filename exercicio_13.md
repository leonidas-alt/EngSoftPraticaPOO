# Exercício 13 - Princípio da Substituição de Liskov (LSP)

## Objetivo
Aplicar o terceiro princípio SOLID - Liskov Substitution Principle (LSP).

## Descrição do Exercício
Implemente uma hierarquia de classes que respeite o LSP, onde objetos de classes derivadas possam substituir objetos da classe base sem quebrar a funcionalidade.

### Requisitos:

1. **Crie a classe base** `Veiculo` com métodos:
   - `acelerar()`: aumenta velocidade
   - `frear()`: diminui velocidade
   - `get_velocidade()`: retorna velocidade atual

2. **Implemente classes derivadas**:
   - **Carro**: velocidade máxima 180 km/h
   - **Bicicleta**: velocidade máxima 50 km/h
   - **Aviao**: velocidade máxima 900 km/h

3. **Crie a classe** `ControladorTrafego` que funciona com qualquer veículo.

4. **Garanta** que todas as subclasses mantêm o comportamento esperado da classe base.

## Entrega
Crie um arquivo chamado `respExercicio13.py` com a implementação seguindo o LSP.

## Exemplo de Uso
```python
def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo).__name__}")
    veiculo.acelerar()
    veiculo.acelerar()
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear()
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")

# Todos os veículos devem funcionar da mesma forma
carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

testar_veiculo(carro)
testar_veiculo(bicicleta)
testar_veiculo(aviao)
```

## Exemplo de Saída Esperada
```
Testando Carro
Velocidade: 40 km/h
Velocidade após frear: 20 km/h
Testando Bicicleta
Velocidade: 20 km/h
Velocidade após frear: 10 km/h
```