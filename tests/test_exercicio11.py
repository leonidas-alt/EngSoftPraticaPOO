import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio11(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio11
            self.module = respExercicio11
        except ImportError:
            self.fail("Arquivo respExercicio11.py não encontrado")
    
    def test_classes_existem(self):
        self.assertTrue(hasattr(self.module, 'Funcionario'), "Classe Funcionario não encontrada")
        self.assertTrue(hasattr(self.module, 'CalculadoraSalario'), "Classe CalculadoraSalario não encontrada")
        self.assertTrue(hasattr(self.module, 'GeradorRelatorio'), "Classe GeradorRelatorio não encontrada")
        self.assertTrue(hasattr(self.module, 'RepositorioFuncionario'), "Classe RepositorioFuncionario não encontrada")
    
    def test_funcionario_apenas_dados(self):
        funcionario = self.module.Funcionario("Ana", 5000.0, "Dev")
        self.assertEqual(funcionario.nome, "Ana")
        self.assertEqual(funcionario.salario, 5000.0)
        self.assertEqual(funcionario.cargo, "Dev")
        # Funcionario não deve ter métodos de cálculo, relatório ou persistência
        self.assertFalse(hasattr(funcionario, 'calcular_salario_liquido'))
        self.assertFalse(hasattr(funcionario, 'gerar_relatorio'))
        self.assertFalse(hasattr(funcionario, 'salvar_no_banco'))
    
    def test_calculadora_salario(self):
        funcionario = self.module.Funcionario("Ana", 5000.0, "Dev")
        calculadora = self.module.CalculadoraSalario()
        salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
        self.assertEqual(salario_liquido, 4500.0)
    
    def test_gerador_relatorio(self):
        funcionario = self.module.Funcionario("Ana", 5000.0, "Dev")
        gerador = self.module.GeradorRelatorio()
        relatorio = gerador.gerar_relatorio(funcionario)
        self.assertIn("Ana", relatorio)
        self.assertIn("Dev", relatorio)
        self.assertIn("5000", relatorio)

if __name__ == '__main__':
    unittest.main()