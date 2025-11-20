# Exercício 17 - Padrão Decorator (Estrutural)

## Objetivo
Implementar o padrão de projeto Decorator para adicionar funcionalidades dinamicamente.

## Descrição do Exercício
Crie um sistema de bebidas onde você pode adicionar ingredientes extras usando decorators.

### Requisitos:

1. **Interface base** `Bebida` com métodos:
   - `get_descricao()`: retorna descrição da bebida
   - `get_preco()`: retorna preço da bebida

2. **Bebidas concretas**:
   - **Cafe**: "Café" - R$ 5.00
   - **Cha**: "Chá" - R$ 3.00

3. **Decorator base** `BebidaDecorator` que implementa `Bebida`.

4. **Decorators concretos**:
   - **LeiteDecorator**: adiciona "com Leite" - +R$ 2.00
   - **AcucarDecorator**: adiciona "com Açúcar" - +R$ 0.50
   - **ChantillyDecorator**: adiciona "com Chantilly" - +R$ 3.00

5. **Demonstre** como combinar múltiplos decorators.

## Entrega
Crie um arquivo chamado `respExercicio17.py` com a implementação do padrão Decorator.

## Exemplo de Uso
```python
# Bebida simples
cafe = Cafe()
print(f"{cafe.get_descricao()} - R$ {cafe.get_preco()}")

# Bebida com decorators
cafe_com_leite = LeiteDecorator(cafe)
print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco()}")

# Múltiplos decorators
cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco()}")
```

## Exemplo de Saída Esperada
```
Café - R$ 5.0
Café com Leite - R$ 7.0
Café com Leite com Açúcar com Chantilly - R$ 10.5
```