# Exercício 18 - Padrão Facade (Estrutural)

## Objetivo
Implementar o padrão de projeto Facade para simplificar uma interface complexa.

## Descrição do Exercício
Crie uma facade para simplificar o uso de um sistema complexo de home theater.

### Sistema Complexo Existente:
```python
class Amplificador:
    def ligar(self): pass
    def definir_volume(self, volume): pass

class DVDPlayer:
    def ligar(self): pass
    def reproduzir(self, filme): pass

class Projetor:
    def ligar(self): pass
    def modo_widescreen(self): pass

class Luzes:
    def diminuir(self, nivel): pass

class PipocaPopper:
    def ligar(self): pass
    def fazer_pipoca(self): pass
```

### Requisitos:

1. **Implemente as classes** do sistema complexo com métodos que imprimem suas ações.

2. **Crie a classe** `HomeTheaterFacade` que encapsula a complexidade.

3. **Métodos da facade**:
   - `assistir_filme(filme)`: configura todo o sistema para assistir
   - `fim_filme()`: desliga todos os componentes

4. **Demonstre** a diferença entre usar o sistema diretamente vs. usando a facade.

## Entrega
Crie um arquivo chamado `respExercicio18.py` com a implementação do padrão Facade.

## Exemplo de Uso
```python
# Uso complexo (sem facade)
amplificador = Amplificador()
dvd = DVDPlayer()
projetor = Projetor()
luzes = Luzes()
pipoca = PipocaPopper()

# Muitas chamadas necessárias...
amplificador.ligar()
amplificador.definir_volume(5)
dvd.ligar()
# ... etc

# Uso simples (com facade)
home_theater = HomeTheaterFacade()
home_theater.assistir_filme("Matrix")
home_theater.fim_filme()
```

## Exemplo de Saída Esperada
```
Preparando para assistir Matrix...
Ligando amplificador
Definindo volume para 5
Ligando DVD player
Ligando projetor
Diminuindo luzes para 10%
Ligando pipoqueira
Fazendo pipoca
Reproduzindo Matrix
Filme finalizado!
```