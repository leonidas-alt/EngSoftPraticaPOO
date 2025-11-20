import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio01(unittest.TestCase):
    def setUp(self):
        try:
            import prof_respExercicio01
            self.module = prof_respExercicio01
        except ImportError:
            self.fail("Arquivo respExercicio01.py não encontrado")
    
    def test_classe_aluno_existe(self):
        self.assertTrue(hasattr(self.module, 'Aluno'), "Classe Aluno não encontrada")
    
    def test_classe_disciplina_existe(self):
        self.assertTrue(hasattr(self.module, 'Disciplina'), "Classe Disciplina não encontrada")
    
    def test_aluno_atributos(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        self.assertEqual(aluno.nome, "João")
        self.assertEqual(aluno.matricula, "123")
        self.assertEqual(aluno.curso, "Engenharia")
    
    def test_disciplina_atributos(self):
        disciplina = self.module.Disciplina("POO", "POO001", 60)
        self.assertEqual(disciplina.nome, "POO")
        self.assertEqual(disciplina.codigo, "POO001")
        self.assertEqual(disciplina.carga_horaria, 60)

if __name__ == '__main__':
    unittest.main()