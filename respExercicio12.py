from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10% de desconto para estudantes
    
class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85 # 15% de desconto para funcionários

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20% de desconto para funcionários
    
class ProcessadorPagamento:
    def processar(self, valor, calculadora: CalculadorDesconto):
        return calculadora.calcular(valor)
    
# Uso do sistema
pagamento = ProcessadorPagamento()
valor_original = 1000.0

# Diferentes tipos de desconto
desconto_estudante = DescontoEstudante()
desconto_funcionario = DescontoFuncionario()
desconto_VIP = DescontoVIP()

valor_final1 = pagamento.processar(valor_original, desconto_estudante)
valor_final2 = pagamento.processar(valor_original, desconto_funcionario)
valor_final3 = pagamento.processar(valor_original, desconto_VIP)

print(f"Estudante: R$ {valor_final1}")
print(f"Funcionário: R$ {valor_final2}")
print(f"VIP: R$ {valor_final3}")