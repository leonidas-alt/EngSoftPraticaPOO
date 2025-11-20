# Exercício 15 - Princípio da Inversão de Dependência (DIP)

## Objetivo
Aplicar o quinto princípio SOLID - Dependency Inversion Principle (DIP).

## Descrição do Exercício
Refatore código que depende de implementações concretas para depender de abstrações.

### Código Problemático:
```python
class EmailService:
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class NotificacaoService:
    def __init__(self):
        self.email_service = EmailService()  # Dependência concreta
    
    def notificar(self, mensagem):
        self.email_service.enviar(mensagem)
```

### Requisitos:

1. **Crie uma abstração** `ServicoNotificacao` com método `enviar(mensagem)`.

2. **Implemente diferentes serviços**:
   - **EmailService**: envia por email
   - **SMSService**: envia por SMS
   - **PushService**: envia notificação push

3. **Refatore** `NotificacaoService` para depender da abstração.

4. **Implemente injeção de dependência** no construtor.

5. **Demonstre** como trocar implementações sem modificar o código cliente.

## Entrega
Crie um arquivo chamado `respExercicio15.py` com a implementação seguindo o DIP.

## Exemplo de Uso
```python
# Diferentes implementações podem ser injetadas
email_service = EmailService()
sms_service = SMSService()
push_service = PushService()

# Mesmo código cliente funciona com qualquer implementação
notificador1 = NotificacaoService(email_service)
notificador2 = NotificacaoService(sms_service)
notificador3 = NotificacaoService(push_service)

mensagem = "Bem-vindo ao sistema!"
notificador1.notificar(mensagem)
notificador2.notificar(mensagem)
notificador3.notificar(mensagem)
```

## Exemplo de Saída Esperada
```
Enviando email: Bem-vindo ao sistema!
Enviando SMS: Bem-vindo ao sistema!
Enviando push: Bem-vindo ao sistema!
```