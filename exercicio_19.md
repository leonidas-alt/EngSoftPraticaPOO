# Exercício 19 - Padrão Observer (Comportamental)

## Objetivo
Implementar o padrão de projeto Observer para notificação de mudanças de estado.

## Descrição do Exercício
Crie um sistema de notificações onde múltiplos observadores são notificados quando o estado de um objeto muda.

### Requisitos:

1. **Interface** `Observer` com método `update(temperatura, umidade, pressao)`.

2. **Classe** `EstacaoMeteorologica` (Subject) que:
   - Mantém lista de observadores
   - Permite adicionar/remover observadores
   - Notifica todos quando dados mudam
   - Métodos: `adicionar_observer()`, `remover_observer()`, `notificar_observers()`, `definir_medicoes()`

3. **Observadores concretos**:
   - **DisplayTemperatura**: mostra apenas temperatura
   - **DisplayUmidade**: mostra apenas umidade
   - **DisplayCompleto**: mostra todos os dados

4. **Demonstre** como múltiplos displays são atualizados automaticamente.

## Entrega
Crie um arquivo chamado `respExercicio19.py` com a implementação do padrão Observer.

## Exemplo de Uso
```python
estacao = EstacaoMeteorologica()

# Criando displays
display_temp = DisplayTemperatura()
display_umidade = DisplayUmidade()
display_completo = DisplayCompleto()

# Registrando observadores
estacao.adicionar_observer(display_temp)
estacao.adicionar_observer(display_umidade)
estacao.adicionar_observer(display_completo)

# Mudança de estado notifica todos
estacao.definir_medicoes(25.5, 65.0, 1013.2)
estacao.definir_medicoes(27.0, 70.0, 1015.1)
```

## Exemplo de Saída Esperada
```
Display Temperatura: 25.5°C
Display Umidade: 65.0%
Display Completo: 25.5°C, 65.0%, 1013.2 hPa
Display Temperatura: 27.0°C
Display Umidade: 70.0%
Display Completo: 27.0°C, 70.0%, 1015.1 hPa
```