class Aluno:
    def __init__(self,nome,matricula,curso):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.notas=[]
    def adicionar_nota(self,nota):
        self.notas.append(float(nota))
    def calcular_media(self):
        if len(self.notas)==0:
            return 0
        return sum(self.notas)/len(self.notas)
    def status(self):
        media=self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"

aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)
print(f"Média: {aluno.calcular_media()}")
print(f"Status: {aluno.status()}")