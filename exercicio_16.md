# Exercício 16 - Padrão Adapter (Estrutural)

## Objetivo
Implementar o padrão de projeto Adapter para integrar interfaces incompatíveis.

## Descrição do Exercício
Crie um adapter para integrar um sistema de pagamento externo com interface diferente.

### Cenário:
Você tem um sistema que espera uma interface `ProcessadorPagamento`, mas precisa integrar com um serviço externo `PayPalAPI` que tem interface diferente.

### Requisitos:

1. **Interface esperada pelo sistema**:
```python
class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass
```

2. **Serviço externo** (não pode ser modificado):
```python
class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"
```

3. **Crie o Adapter** `PayPalAdapter` que implementa `ProcessadorPagamento` e usa `PayPalAPI` internamente.

4. **Implemente a classe** `SistemaPagamento` que usa qualquer `ProcessadorPagamento`.

5. **Demonstre** o uso com diferentes processadores.

## Entrega
Crie um arquivo chamado `respExercicio16.py` com a implementação do padrão Adapter.

## Exemplo de Uso
```python
# Sistema funciona com interface padrão
processador_interno = ProcessadorPagamentoInterno()
sistema1 = SistemaPagamento(processador_interno)

# Adapter permite usar PayPal com a mesma interface
paypal_api = PayPalAPI()
paypal_adapter = PayPalAdapter(paypal_api)
sistema2 = SistemaPagamento(paypal_adapter)

# Ambos funcionam da mesma forma
sistema1.realizar_pagamento(100.0, "1234-5678")
sistema2.realizar_pagamento(200.0, "8765-4321")
```