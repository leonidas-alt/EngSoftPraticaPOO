import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio04(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio04 as respExercicio04
            self.module = respExercicio04
        except ImportError:
            self.fail("Arquivo respExercicio04.py não encontrado")
    
    def test_heranca_funcionario(self):
        funcionario = self.module.Funcionario("João", "123", "01/01/1990", "Secretário")
        self.assertIsInstance(funcionario, self.module.Pessoa)
        self.assertEqual(funcionario.cargo, "Secretário")
    
    def test_heranca_tutor(self):
        tutor = self.module.Tutor("Maria", "456", "01/01/1985", "Programação")
        self.assertIsInstance(tutor, self.module.Pessoa)
        self.assertEqual(tutor.area_atuacao, "Programação")
    
    def test_metodo_apresentar_sobrescrito(self):
        tutor = self.module.Tutor("Maria", "456", "01/01/1985", "Programação")
        apresentacao = tutor.apresentar()
        self.assertIn("Programação", apresentacao)

if __name__ == '__main__':
    unittest.main()