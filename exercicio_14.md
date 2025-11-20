# Exercício 14 - Princípio da Segregação de Interface (ISP)

## Objetivo
Aplicar o quarto princípio SOLID - Interface Segregation Principle (ISP).

## Descrição do Exercício
Refatore interfaces "gordas" em interfaces menores e mais específicas.

### Código Problemático:
```python
class Trabalhador:
    def trabalhar(self):
        pass
    
    def comer(self):
        pass
    
    def dormir(self):
        pass
    
    def programar(self):
        pass
```

### Requisitos:

1. **Identifique o problema** da interface atual (nem todos os trabalhadores programam).

2. **Crie interfaces específicas**:
   - **Trabalhavel**: método `trabalhar()`
   - **Alimentavel**: método `comer()`
   - **Descansavel**: método `dormir()`
   - **Programavel**: método `programar()`

3. **Implemente classes concretas**:
   - **Desenvolvedor**: implementa todas as interfaces
   - **Gerente**: implementa Trabalhavel, Alimentavel, Descansavel
   - **Robo**: implementa apenas Trabalhavel e Programavel

4. **Demonstre** como cada classe implementa apenas as interfaces necessárias.

## Entrega
Crie um arquivo chamado `respExercicio14.py` com a implementação seguindo o ISP.

## Exemplo de Uso
```python
from abc import ABC, abstractmethod

desenvolvedor = Desenvolvedor("Ana")
gerente = Gerente("Carlos")
robo = Robo("R2D2")

# Desenvolvedor faz tudo
desenvolvedor.trabalhar()
desenvolvedor.comer()
desenvolvedor.programar()

# Gerente não programa
gerente.trabalhar()
gerente.comer()

# Robô não come nem dorme
robo.trabalhar()
robo.programar()
```