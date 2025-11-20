import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio20(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio20
            self.module = respExercicio20
        except ImportError:
            self.fail("Arquivo respExercicio20.py não encontrado")
    
    def test_classes_existem(self):
        self.assertTrue(hasattr(self.module, 'EstrategiaFrete'), "Interface EstrategiaFrete não encontrada")
        self.assertTrue(hasattr(self.module, 'FreteNormal'), "Classe FreteNormal não encontrada")
        self.assertTrue(hasattr(self.module, 'FreteExpresso'), "Classe FreteExpresso não encontrada")
        self.assertTrue(hasattr(self.module, 'FreteEconomico'), "Classe FreteEconomico não encontrada")
        self.assertTrue(hasattr(self.module, 'CalculadoraFrete'), "Classe CalculadoraFrete não encontrada")
    
    def test_frete_normal(self):
        frete = self.module.FreteNormal()
        valor = frete.calcular_frete(10.0, 100.0)  # peso=10kg, distancia=100km
        esperado = 5.0 + (10.0 * 2.0) + (100.0 * 0.1)  # 5 + 20 + 10 = 35
        self.assertEqual(valor, esperado)
    
    def test_frete_expresso(self):
        frete = self.module.FreteExpresso()
        valor = frete.calcular_frete(10.0, 100.0)
        esperado = 15.0 + (10.0 * 3.0) + (100.0 * 0.2)  # 15 + 30 + 20 = 65
        self.assertEqual(valor, esperado)
    
    def test_frete_economico(self):
        frete = self.module.FreteEconomico()
        valor = frete.calcular_frete(10.0, 100.0)
        esperado = 2.0 + (10.0 * 1.0) + (100.0 * 0.05)  # 2 + 10 + 5 = 17
        self.assertEqual(valor, esperado)
    
    def test_calculadora_frete(self):
        calculadora = self.module.CalculadoraFrete(self.module.FreteNormal())
        valor = calculadora.calcular(10.0, 100.0)
        self.assertEqual(valor, 35.0)
        
        # Trocar estratégia
        calculadora.definir_estrategia(self.module.FreteExpresso())
        valor = calculadora.calcular(10.0, 100.0)
        self.assertEqual(valor, 65.0)

if __name__ == '__main__':
    unittest.main()