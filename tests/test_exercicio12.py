import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio12(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio12
            self.module = respExercicio12
        except ImportError:
            self.fail("Arquivo respExercicio12.py não encontrado")
    
    def test_classes_existem(self):
        self.assertTrue(hasattr(self.module, 'CalculadorDesconto'), "Classe CalculadorDesconto não encontrada")
        self.assertTrue(hasattr(self.module, 'DescontoEstudante'), "Classe DescontoEstudante não encontrada")
        self.assertTrue(hasattr(self.module, 'DescontoFuncionario'), "Classe DescontoFuncionario não encontrada")
        self.assertTrue(hasattr(self.module, 'DescontoVIP'), "Classe DescontoVIP não encontrada")
        self.assertTrue(hasattr(self.module, 'ProcessadorPagamento'), "Classe ProcessadorPagamento não encontrada")
    
    def test_desconto_estudante(self):
        desconto = self.module.DescontoEstudante()
        valor_com_desconto = desconto.calcular(1000.0)
        self.assertEqual(valor_com_desconto, 900.0)  # 10% desconto
    
    def test_desconto_funcionario(self):
        desconto = self.module.DescontoFuncionario()
        valor_com_desconto = desconto.calcular(1000.0)
        self.assertEqual(valor_com_desconto, 850.0)  # 15% desconto
    
    def test_desconto_vip(self):
        desconto = self.module.DescontoVIP()
        valor_com_desconto = desconto.calcular(1000.0)
        self.assertEqual(valor_com_desconto, 800.0)  # 20% desconto
    
    def test_processador_pagamento(self):
        processador = self.module.ProcessadorPagamento()
        desconto_estudante = self.module.DescontoEstudante()
        valor_final = processador.processar(1000.0, desconto_estudante)
        self.assertEqual(valor_final, 900.0)

if __name__ == '__main__':
    unittest.main()